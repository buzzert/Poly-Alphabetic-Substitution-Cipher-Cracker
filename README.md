Poly-Alphabetic Substitution Cipher Cracker
===========================================

Written by: James Magahern <james@magahern.com>

# Known Shortcomings #
* Not very smart at detecting plaintext. Currently uses the
  38th most common English word ("there") as a "crib".
* Currently only bruteforces the cipher. Not very good if the
  keylength is long (but performs not too bad on a keylength of
  3-5 characters)