
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct Pair
{
    char *key;
    char *value;
} Pair;

typedef struct BasicHashTable
{
    int capacity;
    Pair **storage;
} BasicHashTable;

Pair *create_pair(char *key, char *value)
{
    Pair *pair = malloc(sizeof(Pair));
    pair->key = strdup(key);
    pair->value = strdup(value);

    return pair;
}

void destroy_pair(Pair *pair)
{
    if (pair != NULL)
    {
        free(pair->key);
        free(pair->value);
        free(pair);
    }
}

unsigned int hash(char *str, int max)
{
    unsigned long hash = 5381;
    int c;
    unsigned char *u_str = (unsigned char *)str;

    while ((c = *u_str++))
    {
        hash = ((hash << 5) + hash) + c;
    }

    return hash % max;
}

/****
  Fill this in.
  All values in storage should be initialized to NULL
  (hint: look up `calloc`)
 ****/
BasicHashTable *create_hash_table(int capacity)
{
    BasicHashTable *ht = malloc(sizeof(BasicHashTable));
    ht->storage = calloc(capacity, sizeof(Pair *));
    ht->capacity = capacity;

    return ht;
}

/****
  Fill this in.
  If you are overwriting a value with a different key, print a warning.
  Don't forget to free any malloc'ed memory!
 ****/
void hash_table_insert(BasicHashTable *ht, char *key, char *value)
{
    // Hash our key to get an index
    int index = hash(key, ht->capacity); //capacity == how many "buckets" we have
    Pair *pair = create_pair(key, value);

    Pair *stored_pair = ht->storage[index];
    if (stored_pair != NULL)
    { // if the bucket is already full
        if (strcmp(key, stored_pair->key) != 0)
        {
            printf("Warning: we don't have a collision system; going to overwrite prev val!!! \n");
        }
        destroy_pair(stored_pair);
    }
    ht->storage[index] = pair;
}

/****
  Fill this in.
  Don't forget to free any malloc'ed memory!
 ****/
void hash_table_remove(BasicHashTable *ht, char *key)
{
    // Hash our key to get an index
    int index = hash(key, ht->capacity); //capacity == how many "buckets" we have

    // Check if there's a valid entry in our bucket
    if (ht->storage[index] == NULL || strcmp(ht->storage[index]->key, key) != 0)
    {
        fprintf(stderr, "Unable to remove entry with this key: %s \n", key);
    }
    else
    {

        destroy_pair(ht->storage[index]);
        ht->storage[index] = NULL;
    }
}

/****
  Fill this in.
  Should return NULL if the key is not found.
 ****/
char *hash_table_retrieve(BasicHashTable *ht, char *key)
{
    // Hash our key to get an index
    int index = hash(key, ht->capacity); //capacity == how many "buckets" we have
    if (ht->storage[index] != NULL && strcmp(ht->storage[index]->key, key) == 0)
    {

        return ht->storage[index]->value;
    }
    fprintf(stderr, "Unable to find entry with your key: %s \n", key);
    return NULL;
}

/****
  Fill this in.
  Don't forget to free any malloc'ed memory!
 ****/
void destroy_hash_table(BasicHashTable *ht)
{
    for (int i = 0; i < ht->capacity; i++)
    {
        if (ht->storage[i] != NULL)
        {
            destroy_pair(ht->storage[i]);
        }
    }

    free(ht->storage);
    free(ht);
}

#ifndef TESTING
int main(void)
{

    struct BasicHashTable *ht = create_hash_table(16);

    hash_table_insert(ht, "line", "Here today...\n");

    printf("%s", hash_table_retrieve(ht, "line"));

    hash_table_remove(ht, "line");

    if (hash_table_retrieve(ht, "line") == NULL)
    {
        printf("...gone tomorrow. (success)\n");
    }
    else
    {
        fprintf(stderr, "ERROR: STILL HERE\n");
    }

    destroy_hash_table(ht);

    return 0;
}
#endif
