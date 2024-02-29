rsa-wiener-attack
=================

A Python implementation of the Wiener attack on RSA public-key encryption scheme.

It uses some results about continued fractions approximations to infer the private key from public key in the cases the encryption exponent is too small or too large.

## Test

To run test, first install `pytest`

```
pip install pytest
```

Then run

```
pytest tests/
```

## Usage

```python
python3 . [crack|generate]
```

### Generate

```python
python3 . generate <bits> <loop>

# Example
python3 . generate 1024 10

# Default
bits = 1024
loop = 1
```

### Crack

```python
python3 . crack -h

# Example
python3 . crack -n 54140638278188731391 -e 49058638714977711163

python3 . crack -n 54140638278188731391 -e 49058638714977711163 -c 1928373781919

# Required
-n <public key n>
-e <public key e>
```