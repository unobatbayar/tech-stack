# TypeScript Examples

This directory contains TypeScript language examples and tutorials.

## 📖 About TypeScript

TypeScript is a strongly typed superset of JavaScript that compiles to plain JavaScript. It adds static type definitions to JavaScript, providing better tooling and error detection.

## 📁 Contents

- `index.ts` - TypeScript source file example
- `index.js` - Compiled JavaScript output
- `tsconfig.json` - TypeScript configuration
- `readme.md` - Quick reference notes

## 🚀 Quick Start

### Install TypeScript Globally

```bash
npm i -g typescript
```

### Compile TypeScript

```bash
tsc index.ts
```

This will generate `index.js` from `index.ts`.

### Run the Compiled JavaScript

```bash
node index.js
```

### Watch Mode (Auto-compile on changes)

```bash
tsc --watch index.ts
```

## 📚 Resources

- [TypeScript Official Website](https://www.typescriptlang.org/)
- [TypeScript Documentation](https://www.typescriptlang.org/docs/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
- [TypeScript Playground](https://www.typescriptlang.org/play)

## 💡 TypeScript Configuration

The `tsconfig.json` file contains compiler options. Common settings include:
- Target JavaScript version
- Module system
- Strict type checking
- Source maps

## 🔧 Common Commands

```bash
# Compile TypeScript file
tsc index.ts

# Compile with watch mode
tsc --watch index.ts

# Compile entire project
tsc

# Check types without emitting files
tsc --noEmit
```
