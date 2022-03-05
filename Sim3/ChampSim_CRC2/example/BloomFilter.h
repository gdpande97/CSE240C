#include "../inc/champsim_crc2.h"

#include <set>
#include <vector>
#include <array>
#include <cstdint>
#include <string>

/************MurmurHash3_x64_128********************/
#define ROTL64(x,y) rotl64(x,y)

inline uint64_t rotl64 ( uint64_t x, int8_t r )
{
  return (x << r) | (x >> (64 - r));
}   

inline uint64_t getblock ( const uint64_t * p, int i )
{
  return p[i];
}

inline uint64_t fmix64 ( uint64_t k )
{
  k ^= k >> 33;
  k *= 0xff51afd7ed558ccd;
  k ^= k >> 33;
  k *= 0xc4ceb9fe1a85ec53;
  k ^= k >> 33;

  return k;
}

void MurmurHash3_x64_128 ( const void * key, const int len,
                           const uint32_t seed, void * out )
{
  const uint8_t * data = (const uint8_t*)key;
  const int nblocks = len / 16;                                                  
  int i;

  uint64_t h1 = seed;
  uint64_t h2 = seed;

  uint64_t c1 = 0x87c37b91114253d5; //big constant
  uint64_t c2 = 0x4cf5ad432745937f; //big constant

  const uint64_t * blocks = (const uint64_t *)(data);

  for(i = 0; i < nblocks; i++)
  {
    uint64_t k1 = getblock(blocks,i*2+0);
    uint64_t k2 = getblock(blocks,i*2+1);
    
    k1 *= c1; k1  = ROTL64(k1,31); k1 *= c2; h1 ^= k1;
    
    h1 = ROTL64(h1,27); h1 += h2; h1 = h1*5+0x52dce729;
    
    k2 *= c2; k2  = ROTL64(k2,33); k2 *= c1; h2 ^= k2;
    
    h2 = ROTL64(h2,31); h2 += h1; h2 = h2*5+0x38495ab5;
  }

  const uint8_t * tail = (const uint8_t*)(data + nblocks*16);

  uint64_t k1 = 0;
  uint64_t k2 = 0;

  switch(len & 15)
  {
  case 15: k2 ^= (uint64_t)(tail[14]) << 48;
  case 14: k2 ^= (uint64_t)(tail[13]) << 40;
  case 13: k2 ^= (uint64_t)(tail[12]) << 32;
  case 12: k2 ^= (uint64_t)(tail[11]) << 24;
  case 11: k2 ^= (uint64_t)(tail[10]) << 16;
  case 10: k2 ^= (uint64_t)(tail[ 9]) << 8;
  case  9: k2 ^= (uint64_t)(tail[ 8]) << 0;
           k2 *= c2; k2  = ROTL64(k2,33); k2 *= c1; h2 ^= k2;

  case  8: k1 ^= (uint64_t)(tail[ 7]) << 56;
  case  7: k1 ^= (uint64_t)(tail[ 6]) << 48;
  case  6: k1 ^= (uint64_t)(tail[ 5]) << 40;
  case  5: k1 ^= (uint64_t)(tail[ 4]) << 32;
  case  4: k1 ^= (uint64_t)(tail[ 3]) << 24;
  case  3: k1 ^= (uint64_t)(tail[ 2]) << 16;
  case  2: k1 ^= (uint64_t)(tail[ 1]) << 8;
  case  1: k1 ^= (uint64_t)(tail[ 0]) << 0;
           k1 *= c1; k1  = ROTL64(k1,31); k1 *= c2; h1 ^= k1;
  };

  h1 ^= len; h2 ^= len;

  h1 += h2;
  h2 += h1;

  h1 = fmix64(h1);
  h2 = fmix64(h2);

  h1 += h2;
  h2 += h1;

  ((uint64_t*)out)[0] = h1;
  ((uint64_t*)out)[1] = h2;
}


/*********BloomFilter********************/
class BloomFilter {
public:
  BloomFilter();
  BloomFilter(uint64_t size, uint8_t numHashes);
  void add(uint64_t data);
//  static BloomFilter merge(BloomFilter b1, BloomFilter b2);
  bool possiblyContains(uint64_t data) const;
  void clear();
  uint8_t getCount();

  uint64_t getSize();
//  uint8_t getNumHashes();
//  void setSize(uint64_t s);
//  void setNumHashes(uint8_t n);
//  uint64_t getValue();
//  void setValue(uint64_t value);
//  std::string toString();

private:
  uint8_t m_numHashes;
  uint8_t count;
  std::vector<bool> m_bits;
};

BloomFilter::BloomFilter()
      : m_numHashes(6)
      , m_bits(std::vector<bool>(1107, false))
{
 
}

BloomFilter::BloomFilter(uint64_t size, uint8_t numHashes)
      : m_numHashes(numHashes)
      , m_bits(std::vector<bool>(size, false))
{
    count = 0;
}

std::array<uint64_t,2> hashbf(const uint8_t *data, std::size_t len)
{
  std::array<uint64_t, 2> hashValue {0, 0};
  MurmurHash3_x64_128(data, len, 0, hashValue.data());
  return hashValue;
}

inline uint64_t nthHash(uint8_t n, uint64_t hashA, uint64_t hashB, uint64_t filterSize) 
{
    return (hashA + n * hashB) % filterSize;
}

void BloomFilter::add(uint64_t data) 
{
  std::array<uint8_t, 8> data_array {0, 0, 0, 0, 0, 0, 0, 0};
  for(int i = 0; i < 8; i++) {
    data_array[i] = ((data >> (i*8)) & 0x00FF);
  }
  auto hashValues = hashbf(data_array.data(), 8);

  for (int n = 0; n < m_numHashes; n++) 
  {
      m_bits[nthHash(n, hashValues[0], hashValues[1], m_bits.size())] = true;
  }
  count++;
}  

bool BloomFilter::possiblyContains(uint64_t data) const 
{
  std::array<uint8_t, 8> data_array {0, 0, 0, 0, 0, 0, 0, 0};
  for(int i = 0; i < 8; i++) {
    data_array[i] = ((data >> (i*8)) & 0x00FF);
  }
  auto hashValues = hashbf(data_array.data(), 8);

  for (int n = 0; n < m_numHashes; n++) 
  {
      if (!m_bits[nthHash(n, hashValues[0], hashValues[1], m_bits.size())]) 
      {
          return false;
      }
  }

  return true;
}

void BloomFilter::clear()
{
    count = 0;
    for (uint64_t i=0; i<m_bits.size();i++ )
        m_bits[i] = false;
}

uint8_t BloomFilter::getCount()
{
    return count;
}

uint64_t BloomFilter::getSize()
{
    return m_bits.size();
}
