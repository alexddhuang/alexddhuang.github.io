---
title: "Reading Fluent Python"
categories: IT
tags: python
toc: true
---

[*Fluent Python: Clear, Concise, and Effective Programming*](http://shop.oreilly.com/product/0636920032519.do) (2015) by [Luciano Ramalho](https://github.com/ramalho) is for practicing Python programmers who want to become proficient in Python 3.

## Part I. Prologue

### Chapter 1. The Python Data Model

#### A Pythonic Card Deck

```python
import collections

# collections.namedtuple returns a named tuple-like class.
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
```

The `FrechDeck` class has only three special methods, but we do many things on it by using the standard library:

- Calculating its length.

    ```python
    >>> deck = FrenchDeck()
    >>> len(deck)
    52
    ```

- Getting a specific card.

    ```python
    >>> deck[0]
    Card(rank='2', suit='spades')
    >>> deck[1]
    Card(rank='3', suit='spades')
    ```

- Choosing a random card.

    ```python
    >>> from random import choice
    >>> choice(deck)
    Card(rank='5', suit='hearts')
    >>> choice(deck)
    Card(rank='4', suit='diamonds')
    ```

- Slicing.

    ```python
    >>> deck[:3]
    [Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')]
    ```

- Iterating.

    ```python
    for card in deck:
        print(card)

    for card in reversed(deck):
        print(card)
    ```

- Checking whether a card is in the deck.

    ```python
    >>> Card('Q', 'hearts') in deck
    True
    >>> Card('7', 'beasts') in deck
    False
    ```

Amazing, consistent, and elegant.

#### How Special Methods Are Used

Special methods are called by the interpreter, not by the programmer.

Let's look at how CPython implements `len()`.

In [`Python/clinic/bltinmodule.c.h`](https://github.com/python/cpython/blob/4901fe274bc82b95dc89bcb3de8802a3dfedab32/Python/clinic/bltinmodule.c.h), we found these lines:

```c
#define BUILTIN_LEN_METHODDEF    \
    {"len", (PyCFunction)builtin_len, METH_O, builtin_len__doc__},
```

So we know that when the interpreter parses `len()`, it will call [`builtin_len`](https://github.com/python/cpython/blob/6a650aaf7735e30636db2721247f317064c2cfd4/Python/bltinmodule.c#L1545):

```c
static PyObject *
builtin_len(PyObject *module, PyObject *obj)
{
    Py_ssize_t res;

    res = PyObject_Size(obj);
    if (res < 0) {
        assert(PyErr_Occurred());
        return NULL;
    }
    return PyLong_FromSsize_t(res);
}
```

Let's continue to dive into [`PyObject_Size`](https://github.com/python/cpython/blob/d33e46d17d33f9b918846982c02ddc17d897c9bc/Objects/abstract.c#L46):

```c
Py_ssize_t
PyObject_Size(PyObject *o)
{
    PySequenceMethods *m;

    if (o == NULL) {
        null_error();
        return -1;
    }

    m = o->ob_type->tp_as_sequence;
    if (m && m->sq_length) {
        Py_ssize_t len = m->sq_length(o);
        assert(len >= 0 || PyErr_Occurred());
        return len;
    }

    return PyMapping_Size(o);
}
```

The [`PyObject`](https://github.com/python/cpython/blob/f7d72e48fb235684e17668a1e5107e6b0dab7b80/Include/object.h#L108) structure is defined in `Include/object.h`:

```c
typedef struct _object {
    _PyObject_HEAD_EXTRA
    Py_ssize_t ob_refcnt;
    struct _typeobject *ob_type;
} PyObject;
```