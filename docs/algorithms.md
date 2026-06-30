# Algorithms

## QuadTree

### Purpose

Organize driver locations to reduce the search space during ride matching.

### Complexity

- Insert: **O(log N)** (average)
- Region Query: **O(log N)** (average)

### Used For

- Storing driver locations
- Finding nearby drivers before selecting the closest one

---

## Euclidean Distance

### Purpose

Calculate the distance between a passenger and nearby drivers.

### Complexity

- **O(K)**, where **K** is the number of nearby drivers returned by the QuadTree.

### Formula

```
distance = √((x₂ - x₁)² + (y₂ - y₁)²)
```

---

## Planned Improvements

### A* Search

**Purpose**

Find the shortest route between pickup and destination using a road network.

**Status:** Planned

---

### Priority Queue

**Purpose**

Rank candidate drivers based on multiple factors such as distance and availability.

**Status:** Planned