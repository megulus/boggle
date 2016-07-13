# Boggle Game

## Overview

This is a Python implementation of the classic Boggle word-search game (by Hasbro). The first version of the game implements the "New Boggle" variant (see 'Boggle Variants'). Other Boggle and scoring variants (see 'scoring variants') to come in future versions.

A boggle board has 16, 25 or 36 lettered dice, depending on the version. The dice are arranged in a square and shuffled at the beginning of a game. The player then has 3 minutes to find as many words as possible on the board. A valid word must:
 * be at least 3 letters long in Classic/New Boggle (4 letters long in more challenging variants)
 * be formed from adjacent (in any direction), non-repeating dice
 * be a standard Enlgish word (no abbreviations, proper names, etc.)


A word of the minimum length (according to the scoring variant used) is worth 1 point, and so on up.

### Current Implementation

The current implementation is a simple command-line version of New Boggle (see Boggle Variants). It prints a 4x4 grid of letters. The player has three minutes to enter words via the command line. The player's input is first screened for the minimum word length; if it passes, it is added to a set (so that duplicate entries are automatically screened out). After time is up, the words in the set are validated (i.e., that their paths on the board are made up of adjacent, non-repeated tiles and the words themselves are standard English words according to the PyEnchant library).


### Future Improvements


 * <s>**HIGH PRIORITY**: Fix bug preventing game from ending if user does nothing.</s> Fixed.
 * Add feature to save top 10 scores and display them when game finishes (a la 1980s arcade games)
 * Add function that finds all words on board for "play-the-computer" version of game
 * Version that allows choice of board versions (Classic, Big Boggle, Super Big Boggle)
 * Implement multi-player version
 * Version that allows choice of alternate scoring variants for multi-player game (Unique Words Scoring, Word Wagering)
 * GUI or web-based version


## Scoring Variants

I don't know whether some of these scoring variants are part of the official rules of the game, but they can allow the user to make the multi-player game more challenging.

### Single-Player Scoring

##### Simple Scoring
 * This is implemented in the basic version of the game. It simply scores all of the valid words entered by the user (minimum-length word = 1 point, etc.)

##### Play the Computer
 * In this version, your score is compared to the theoretical maximum score (for all the possible words on the board)

### Multi-Player Scoring

##### Simple Multi-Player Scoring

The player with the most points wins the game.

##### Unique Words Scoring

Only words that an individual player has found (and no other player) count towards that player's score.

##### Word Wagering

Each player must guess:
  * a word that only he/she has found
   * if guessed correctly, 2X the word's point value will be added to the player's score
   * *the catch*: if wrong, 2X that word's value is *subtracted* from the player's score
  * a word that everyone will have found
   * if all other players have found the word *and* no other player has guessed the same word for this category, the player gets 2X the word's point value added to their score
   * if all other players have found the word, but another player has also guessed that everyone would find it, all players who have guessed the word lose one point
   * if at least one other player has not found the word, the player who guessed it loses 2X the word's point value


## Boggle Variants

As I discovered when I started researching boggle letter frequency, there are multiple versions of Boggle, which are:
- Classic Boggle
- New Boggle
- Big Boggle
- Super Big Boggle

Classic Boggle was developed in the 1970s. It uses 16 dice (4x4 board) with the following letter combinations:

```
AACIOT
ABILTY
ABJMOQu
ACDEMP
ACELRS
ADENVZ
AHMORS
BIFORX
DENOSW
DKNOTU
EEFHIY
EGKLUY
EGINTV
EHINPS
ELPSTU
GILRUW
```

New Boggle (the version sold since ~2008, according to the internet) was created to address some problems in the letter
frequency of Classic Boggle. Its 16 dice have the following letter combinations:

```
AAEEGN
ABBJOO
ACHOPS
AFFKPS
AOOTTW
CIMOTU
DEILRX
DELRVY
DISTTY
EEGHNW
EEINSU
EHRTVW
EIOSST
ELRTTY
HIMNUQu
HLNNRZ
```

Big Boggle has 25 dice (5x5 board) with the following letter combinations:

```
aaafrs
aaeeee
aafirs
adennn
aeeeem

aeegmu
aegmnn
afirsy
bjkqxz
ccenst

ceiilt
ceilpt
ceipst
ddhnot
dhhlor

dhlnor
dhlnor
eiiitt
emottt
ensssu

fiprsy
gorrvw
iprrry
nootuw
ooottu
```

Super Big Boggle has 36 dice (6x6 board) with the following letter combinations:

```
AAAFRS
AAEEEE
AAEEOO
AAFIRS
ABDEIO
ADENNN

AEEEEM
AEEGMU
AEGMNN
AEILMN
AEINOU
AFIRSY

AnErHeInQuTh
BBJKXZ
CCENST
CDDLNN
CEIITT
CEIPST

CFGNUY
DDHNOT
DHHLOR
DHHNOW
DHLNOR
EHILRS

EIILST
EILPST
EIO###
EMTTTO
ENSSSU
GORRVW

HIRSTV
HOPRST
IPRSYY
JKQuWXZ
NOOTUW
OOOTTU
```