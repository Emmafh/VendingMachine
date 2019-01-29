[TOC]

#README.md

## Assumptions

1. Only one user can get access to the vending machine at one time, which means there can only be one process in the vending machine.
2. The user can only choose one product during one transaction.
3. The user should insert coins before he can choose the product.
4. The deal is triggered when the user choose the product.
5. The types of four coins: 10, 5, 2, 1， the initial store of the four coins in the vending machien are 5, 5, 5, 5
6. The types of four products are: A, B, C, D, the initial number of the four products are 1, 3, 3, 3
7. The prices of the products are 25, 13, 8, 12
8. If there are not enough coins to give back changes, then the deal will fail.
9. To save time, I just do the unit test for customer user cases.

## Introduction

1. Need to be executed with python > 2.7

2. You can go into the root folder and run the following command:

   ```bash
   python main.py
   ```

3. You can run the unit test with the file: run_unit_test.sh, or run the command in the root folder:

   ```bash
   python -m unittest discover -s tests -p "*Test.py"
   ```

## User cases

### Admin user cases

1. Add or delete product store
2. Add or delete coins store

### Customer user cases

State 1: initial state, before inserting coins:

- select product   --->   tell user to insert coins at first
- insert coins  --->  switch to state 2
- return coins  ---> no coins to return

State 2: After inserting coins:

- select product ---> trigger the deal ---> switch to state 1
- insert coins 
- return coins ---> return all coins  ---> switch to state1

## Code structures

I have taken advantage of State design pattern and Singleton design pattern. Here is the structure of the code.

```
├── README.md
├── main.py   // entrance
├── run_unit_test.sh  // run unit test
├── tests
│   ├── __init__.py
│   ├── acceptCoinsStateTest.py
│   ├── dataTest.py
│   ├── initStateTest.py
│   └── vendingMachineTest.py
└── vm
    ├── __init__.py
    ├── acceptCoinsState.py		//VendingMachine's state after accepting coins
    ├── data.py		//The Singleton class for storing data
    ├── initState.py	//The initial state of the vending machine
    ├── state.py		//The interface of state
    └── vendingMachine.py	// Vending Machine class
```

