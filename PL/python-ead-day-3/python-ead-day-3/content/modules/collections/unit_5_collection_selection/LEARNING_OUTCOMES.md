# Unit 5: Collection Selection Guide - Learning Outcomes

## Overview
By completing this unit, you will master the art of choosing the right Python data structure for any scenario. This is a critical engineering skill that impacts performance, memory usage, and code readability. You'll compare Lists, Tuples, Dictionaries, and Sets side-by-side to determine the optimal choice for healthcare and financial data models.

**Estimated Time**: 3-4 hours total
- Knowledge: 40 min
- Check Your Understanding: 20 min
- Case Study Analysis: 60-90 min
- Capstone Lab: 2 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### Decision Making & Architecture

- [ ] **Evaluate** data requirements based on Order, Mutability, and Uniqueness.
- [ ] **Choose** the optimal data structure for a given business problem.
- [ ] **Assess** the trade-offs between different collection types.
- [ ] **Justify** architectural decisions using performance characteristics (Big O notation).

### Performance Benchmarking

- [ ] **Compare** membership test speeds across all collection types.
- [ ] **Identify** "Linear Scan" bottlenecks in existing code.
- [ ] **Analyze** memory footprints of different data structures.
- [ ] **Optimize** data retrieval by switching from lists to dictionaries/sets.

### Selection Scenarios

- [ ] **Identify** when to use **Lists**: For ordered sequences where position matters and items may repeat.
- [ ] **Identify** when to use **Tuples**: For fixed record types, returning multiple values, or as dictionary keys.
- [ ] **Identify** when to use **Dictionaries**: For fast lookups via unique identifiers (IDs, Codes).
- [ ] **Identify** when to use **Sets**: For deduplication and high-speed existence checks.

### Hybrid Collections

- [ ] **Design** nested structures (e.g., list of dictionaries, dictionary of sets).
- [ ] **Model** complex healthcare relationships (e.g., Patient ID mapping to a set of Unique Allergies).
- [ ] **Normalize** data by choosing appropriate levels of nesting.

### Best Practices

- [ ] **Apply** the "Principle of Least Power": Choose the simplest structure that satisfies requirements.
- [ ] **Favor** immutability (Tuples) where data safety is concerned.
- [ ] **Prioritize** readability: sometimes a clear List is better than a complex, over-engineered nested Set.

### Real-World Application

- [ ] **Design** a patient queuing system (List).
- [ ] **Architect** a drug interaction lookup table (Dictionary).
- [ ] **Implement** a unique lab result tracker (Set).
- [ ] **Represent** fixed patient metadata (Tuple).

---

## Assessment Criteria

### Selection Case Studies (Pass: Correct logic and justification)
- Successfully analyze 5 real-world scenarios and select the correct structure.
- Provide a clear performance-based justification for each choice.

### Capstone Lab (Pass: 80% or higher)
- **Problem Solving**: Implementation of a multi-structure healthcare dashboard.
- **Performance**: Code must pass specific time-complexity requirements for large datasets.
- **Maintainability**: Clear naming and logical nesting of data structures.

---

## Next Steps

After mastering collection selection:
1. **Move to Module 2: OOP** to learn how to encapsulate these collections within classes.
2. **Apply** these selection skills in your final module project.
3. **Explore** specialized collections like `deque`, `Counter`, and `OrderedDict`.

---

## Decision Matrix

| Requirement | Use This | Why |
|-------------|----------|-----|
| I need to maintain order | **List** or **Tuple** | Positional indices |
| I need to prevent changes | **Tuple** | Immutability |
| I need fast lookups by ID | **Dictionary** | O(1) hashing |
| I need to remove duplicates | **Set** | Uniqueness enforcement |
| I need to group data pairs | **Dictionary** | Key-Value mapping |

---

## Self-Assessment Questions

Before moving to the next module, can you:

1. Explain why choosing a list for 1 million membership checks is a bad idea?
2. Pick the right structure for storing a patient's GPS coordinates (Latitude, Longitude)?
3. Decide between a Dictionary and a List for an appointment calendar?
4. Explain when a Set is better than a Dictionary?
5. Design a structure to store "Doctors and the list of unique patients they saw today"?

If you answered "yes" to all, you've mastered Python Collections! 🏆
