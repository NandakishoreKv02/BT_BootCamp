# Unit 2.2: Why Object-Oriented Programming? - Learning Outcomes

## Overview
This unit focuses on the "Business Case" for OOP. While Unit 2.1 showed *how* to transition from procedural code, Unit 2.2 explains *why* the world's most critical systems—from Electronic Health Records (EHR) to Banking Cores—are built on Object-Oriented principles. We will evaluate how OOP manages the "Three Devils of Software": Complexity, Change, and Scale.

**Estimated Time**: 8-10 hours
- Knowledge: 2 hours
- Exercises: 3 hours
- App Labs: 3-5 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### Strategic Understanding
- [ ] **Justify** the use of OOP for large-scale systems using the principles of Modularity and Encapsulation.
- [ ] **Contrast** the impact of change in Procedural vs. Object-Oriented architectures (The "Ripple Effect").
- [ ] **Identify** specific Healthcare domain challenges (e.g., interoperability, patient privacy) that are best solved with OOP.

### Architectural Principles
- [ ] **Define** Reusability and explain how "Pluggable" components reduce development costs.
- [ ] **Explain** Extensibility and how code can be "Open for Extension, Closed for Modification."
- [ ] **Analyze** Scalability from both a code-maintenance and a team-distribution perspective.

### Paradigm Comparison
- [ ] **Compare** Procedural, Functional, and Object-Oriented paradigms for a given set of requirements.
- [ ] **Select** the appropriate paradigm based on the "State vs. Transformation" nature of a problem.

---

## Assessment Criteria

### Exercises (Pass: All tests passing)
- Correct categorization of scenarios into Modularity, Reusability, or Maintainability.
- Analysis of "Spaghetti Code" snippets to identify breaking points in scalability.
- Decision-making exercises choosing between Functional and OO approaches.

### App Labs (Pass: 80% or higher)
- **Separation of Concerns**: Demonstrating modularity by keeping data-access, logic, and presentation separate.
- **Component Reusability**: Creating a clinical utility (e.g., a Logger or Config Manager) that works across multiple labs.
- **Scalability Design**: Designing a system that can handle an increasing amount of "Nouns" without refactoring the core logic.

---

## Next Steps
1. **Unit 2.3: Classes and Objects**: Transitioning from "Thinking in Objects" to "Building with Classes."

---

## Common Pitfalls to Avoid
✅ **Do**: Think about the long-term cost of maintenance (Code is read 10x more than it is written).

❌ **Don't**: Assume "Reusability" means just Copy-Pasting functions; think about interface stability.

✅ **Do**: Recognize that OOP is an overhead that pays for itself only at scale.

❌ **Don't**: Use the complexity of OOP for small, one-off clinical calculators.
