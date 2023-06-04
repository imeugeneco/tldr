# TypeScript 5.1

https://devblogs.microsoft.com/typescript/announcing-typescript-5-1/



## What's New

* **Easier Implicit Returns for `undefined`-Returning Functions**
* **Unrelated Types for Getters and Setters**
* Decoupled Type-Checking Between JSX Elements and JSX Tag Types
* Namespaced JSX Attributes
* **`typeRoots` Are Consulted In Module Resolution**
* Linked Cursors for JSX Tags
* Snippet Completions for `@param` JSDoc Tags
* Optimizations
* **Breaking Changes**

<br>



### Easier Implicit Returns for undefined-Returning Functions

* TypeScript 5.1 now allows `undefined`-returning functions to have no return statement.

```ts
// ✅ Works in TypeScript 5.1!
function f4(): undefined {
    // no returns
}

// ✅ Works in TypeScript 5.1!
takesFunction((): undefined => {
    // no returns
});
```

* If a function has no return expressions and is being passed to something expecting a function that returns `undefined`, TypeScript infers `undefined` for that function’s return type.

```ts
// ✅ Works in TypeScript 5.1!
takesFunction(function f() {
    //                 ^ return type is undefined

    // no returns
});

// ✅ Works in TypeScript 5.1!
takesFunction(function f() {
    //                 ^ return type is undefined

    return;
});
```

<br>



### Unrelated Types for Getters and Setters

* TypeScript 5.1 now allows completely unrelated types for `get` and `set` accessor properties, provided that they have explicit type annotations. 
* This also allows other patterns like requiring `set` accessors to accept only "valid" data, but specifying that `get` accessors may return `undefined` if some underlying state hasn’t been initialized yet.

```ts
class SafeBox {
    #value: string | undefined;

    // Only accepts strings!
    set value(newValue: string) {

    }

    // Must check for 'undefined'!
    get value(): string | undefined {
        return this.#value;
    }
}
```

<br>



### Breaking Changes

* **ES2020 and Node.js 14.17 as Minimum Runtime Requirements**: TypeScript 5.1 now only runs on Node.js 14.17 and later due to its reliance on JavaScript functionality introduced in ECMAScript 2020. Running TypeScript 5.1 under older versions of Node.js may lead to errors.

* **Explicit `typeRoots` Disables Upward Walks for `node_modules/@types`**:  If the `typeRoots` option is specified in a `tsconfig.json` but resolution to any `typeRoots` directories has failed, TypeScript will no longer continue walking up parent directories, trying to resolve packages within each parent’s `node_modules/@types` folder. 





