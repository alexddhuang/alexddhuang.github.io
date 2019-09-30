---
title: "Notes on C# in Depth, 4th Edition"
categories: IT
tags: csharp dotnet
toc: true
---

[*C# in Depth*, 4th Edition](https://csharpindepth.com/). [Jon Skeet](https://codeblog.jonskeet.uk/). 2019.

## Part 2. C# 2–5

2005 ~ 2012.

### Chapter 2. C# 2

#### 2.1 Generics

Where are generics most heavily used for?

- Collections
- Delegates, particularly in LINQ
- Asynchronous code
- Nullable value types

Example: Generating and printing names.

- Using arrays

    ```c#
    static string[] GenerateNames() {
        string[] names = new string[4]; 
        names[0] = "Gamma";
        names[1] = "Vlissides"; 
        names[2] = "Johnson";
        names[3] = "Helm";
        return names;
    }

    static void PrintNames(string[] names) {
        foreach (string name in names) {
            Console.WriteLine(name);
        }
    }
    ```

    The main drawback of using arrays is that its size is static (specified at compile time).

- Using `ArrayList`

    ```c#
    static ArrayList GenerateNames() {
        ArrayList names = new ArrayList(); 
        names.Add("Gamma"); 
        names.Add("Vlissides"); 
        names.Add("Johnson"); 
        names.Add("Helm");
        return names;
    }

    static void PrintNames(ArrayList names) {
        foreach (string name in names) {
            Console.WriteLine(name);
        }
    }
    ```

    The size of `ArrayList` is dynamic. However, the `PrintNames` method is **not safe** because `ArrayList` can contains any `Object`, not just `string`s.

- Using `StringCollection`

    ```c#
    static StringCollection GenerateNames() {
        StringCollection names = new StringCollection(); 
        names.Add("Gamma");
        names.Add("Vlissides");
        names.Add("Johnson");
        names.Add("Helm");
        return names;
    }

    static void PrintNames(StringCollection names) {
        foreach (string name in names) {
            Console.WriteLine(name);
        }
    }
    ```

    Now `PrintNames` is safe, but the code is not flexible. What if you want a collection of other types? Such as `PlayerCollection`, `StarCollection`, or `DogCollection`. The C# standard library doesn't provide these classes, so you have to respectively define them. That's a lot of works.

- Using `List<T>`

    ```c#
    static List<string> GenerateNames() {
        List<string> names = new List<string>(); 
        names.Add("Gamma"); 
        names.Add("Vlissides"); 
        names.Add("Johnson");
        names.Add("Helm");
        return names;
    }

    static void PrintNames(List<string> names) {
        foreach (string name in names) {
            Console.WriteLine(name);
        }
    }
    ```

    `List<T>` solves all problems mentioned above.
