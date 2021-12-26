# Multiton pattern

Also known as Registry.

## The What

Multiton pattern is a **Creational** design pattern that generalizes the singleton pattern.
It ensures that only one object will be created for a Key.
Objects created for specif keys are kept in a pool.
Asking for an object, given a specific key, would create that object and store it in the pool, if key is not in pool.
Else it would return the object kept in the pool and referred to by the key.

## The Why / When

Just like the Singleton pattern, the Multiton pattern solves the problem of having uncontrolled number of instances of a class, and extends by allowing a controlled number of a class instances for each given value.
The most common reason for this is to control access to shared resources by providing a **global** access point to these instances.

## The But

Look out for race condition and Make it thread safe for **multithreaded** systems, two threads can enter the **"if condition"**, ie **_if key not in pool, then create instance_** resulting in the creation of multiple instances for a single key, defeating the purpose of the pattern and producing possible leakage.

This pattern, like the Singleton pattern, makes unit testing far more difficult,[1] as it introduces global state into an application.

## The example

**Shared file context managers.**
In this example, we implement the multiton pattern to provide a global shared file context manager for each file.
This limits the number of opened files, by sharing the open instance per file.
And allows controll over concurrent operations on shared file managers, for example can only write if only one actor has the file open.
