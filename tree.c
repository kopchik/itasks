#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <strings.h>

typedef int value_t;

struct Node {
  value_t value;
  struct Node *left;
  struct Node *right;
};
typedef struct Node Node;

Node *newnode(value_t value) {
  Node *node = malloc(sizeof(Node));
  assert(node);
  bzero(node, sizeof(Node));
  node->value = value;
  return node;
}

void insert(Node *root, Node *node) {
  if (node->value >= root->value) {
    if (node->right) {
      insert(node->right, node);
    } else {
      node->right = node;
    }
  } else {
    if (node->left) {
      insert(node->left, node);
    } else {
      node->left = node;
    }
  }
}

int main(void) {
  Node *root = newnode(0);
  insert(root,  newnode(2));
  return 0;
}
