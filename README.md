# cryptography-game

During the cryptography game you will be guided through exercises that will lead you to a real-life case of message exchange. The two protagonists of the game are Alice and Bob ( yes always them ). The game consists of three levels. In the first you will have to figure out how to implement a simple encryption algorithm. In the second you will calculate a secret key that the two players will know without having to exchange it. In the last trial of the game you will put all the concepts learned together and have to encrypt and decrypt messages.

## Exercise 1

This exercise provides some tests that currently fail. The idea is to use a system similar to Caesar's cipher to decode these messages. In the first phase of the exercise you will not have the shared alphabet but only the symbols it contains, which are:

- Lowercase and uppercase letters
- Numbers
- Special characters ( ,.'?!$\*&@:+)

in the second part of the exercise you will be provided with the shared alphabet, this will demonstrate how much easier it is to decode and encode a message with a shared piece of information.

## Exercise 2

In this exercise we will use the Diffie Hellman algorithm to generate the public and private keys. You will have at your disposal the public generators G and p and the secrets of those who must generate a public key and a private key. In the same way of the first exercise, you have some unit test and you must pass all the test to complete the exercise.
According the Diffie Hellamn algorithm the formulas you have to evaluate are:

- public_key = PUBLIC_G $^{secret}$ $\bmod$ PUBLIC_P

- private_key = public_key $^{secret}$ $\bmod$ PUBLIC_P

## Exercise 3

In the last exercise you have to interject a conversation between Alice and Bob. The messages that the two exchanged are represented by the file "exercise3.txt". In this case we want to read the messages Alice is sending to Bob. There is a problem, in some cases we were able to read Bob's secret and in others we were not. Try to decode the message ! :)
