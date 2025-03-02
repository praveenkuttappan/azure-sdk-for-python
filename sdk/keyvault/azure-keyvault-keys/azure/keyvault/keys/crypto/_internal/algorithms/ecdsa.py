# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric import utils

from ..algorithm import SignatureAlgorithm
from ..transform import SignatureTransform
from ..._enums import SignatureAlgorithm as KeyVaultSignatureAlgorithm


class _EcdsaSignatureTransform(SignatureTransform):
    def __init__(self, key, hash_algorithm):
        super(_EcdsaSignatureTransform, self).__init__()

        self._key = key
        self._hash_algorithm = hash_algorithm

    def sign(self, digest):
        return self._key.sign(digest, ec.ECDSA(utils.Prehashed(self._hash_algorithm)))

    def verify(self, digest, signature):
        return self._key.verify(signature, digest, ec.ECDSA(utils.Prehashed(self._hash_algorithm)))


class _Ecdsa(SignatureAlgorithm):
    def create_signature_transform(self, key):
        return _EcdsaSignatureTransform(key, self.default_hash_algorithm)


class Ecdsa256(_Ecdsa):
    _name = KeyVaultSignatureAlgorithm.es256_k
    _default_hash_algorithm = hashes.SHA256()
    coordinate_length = 32


class Es256(_Ecdsa):
    _name = KeyVaultSignatureAlgorithm.es256
    _default_hash_algorithm = hashes.SHA256()
    coordinate_length = 32


class Es384(_Ecdsa):
    _name = KeyVaultSignatureAlgorithm.es384
    _default_hash_algorithm = hashes.SHA384()
    coordinate_length = 48


class Es512(_Ecdsa):
    _name = KeyVaultSignatureAlgorithm.es512
    _default_hash_algorithm = hashes.SHA512()
    coordinate_length = 66


Ecdsa256.register()
Es256.register()
Es384.register()
Es512.register()
