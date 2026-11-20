"""There are 7 bus stops:
S1  S2  S3  S4  S5  S6  S7


The bus must:
- Stop at exactly 3 stops.
- Never stop at two consecutive stops.
- Find all possible combinations.
For example:

Valid
 S1 S3 S5

Because no selected stops are consecutive.

Invalid
 S1 S2 S5

Because S1 and S2 are consecutive.
2. Think of it as an array
We can represent the stops using numbers:
arr = [1, 2, 3, 4, 5, 6, 7]



We need to select exactly 3 elements."""

