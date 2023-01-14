{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOt5TR7A3VlrCD75RmNofbH"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Z-wTFFIgkHoO",
        "outputId": "df3d5dc0-e439-4178-dd12-6fa91b070bc6"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "CBTF\n",
            "BASE\n"
          ]
        }
      ],
      "source": [
        "def encrypt(key, plaintext):\n",
        "    ciphertext=\"\"\n",
        "    #iterate over given text\n",
        "    for i in range(len(plaintext)):\n",
        "        char = plaintext[i]\n",
        "        ciphertext += chr((ord(char) + key-65) % 26 + 65)\n",
        "\n",
        "    return ciphertext\n",
        "\n",
        "def decrypt(key,ciphertext):\n",
        "    plaintext=\"\"\n",
        "    #upper case letters for decryption\n",
        "    alphabet=\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"\n",
        "    #iterate over given text\n",
        "    for char in ciphertext:\n",
        "      pos = alphabet.find(char)\n",
        "      decrypted_pos = (pos - key) % 26\n",
        "      decrypted_char = alphabet[decrypted_pos]\n",
        "      plaintext += decrypted_char\n",
        "    return plaintext\n",
        "\n",
        "a = encrypt(1, \"BASE\")\n",
        "print(a)\n",
        "\n",
        "b = decrypt(1, a)\n",
        "print(b)\n"
      ]
    }
  ]
}