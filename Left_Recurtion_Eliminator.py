#!/usr/bin/env python3
"""
Left Recursion Elimination Algorithm
Based on Aho et al. 2006, Section 4.3.3, Algorithm 4.19
"""

def parse_grammar(lines):
    """
    Parse grammar from input lines.
    Returns: dict mapping nonterminal -> list of production alternatives
    """
    grammar = {}
    for line in lines:
        line = line.strip()
        if not line or '->' not in line:
            continue
        
        parts = line.split('->')
        nonterminal = parts[0].strip()
        productions = parts[1].strip().split()
        
        grammar[nonterminal] = productions
    
    return grammar


def is_nonterminal(symbol):
    """Check if a symbol is a nonterminal (uppercase letter)"""
    return symbol and symbol[0].isupper()


def has_immediate_left_recursion(nonterminal, productions):
    """
    Check if a nonterminal has immediate left recursion.
    Immediate left recursion: A -> Aα
    """
    for prod in productions:
        if prod and prod[0] == nonterminal:
            return True
    return False


def eliminate_immediate_left_recursion(nonterminal, productions, used_nonterminals):
    """
    Eliminate immediate left recursion from a nonterminal.
    
    Transform:
        A -> Aα₁ | Aα₂ | ... | Aαₘ | β₁ | β₂ | ... | βₙ
    Into:
        A -> β₁A' | β₂A' | ... | βₙA'
        A' -> α₁A' | α₂A' | ... | αₘA' | ε
    
    Returns: updated grammar dict and updated used_nonterminals set
    """
    # Separate productions into recursive and non-recursive
    recursive = []  # Productions starting with A (A -> Aα)
    non_recursive = []  # Productions not starting with A (A -> β)
    
    for prod in productions:
        if prod and prod[0] == nonterminal:
            # Remove the leading nonterminal to get α
            alpha = prod[1:]
            recursive.append(alpha)
        else:
            non_recursive.append(prod)
    
    # If no immediate left recursion, return original
    if not recursive:
        return {nonterminal: productions}, used_nonterminals
    
    # If all productions are recursive (no β), this shouldn't happen with valid input
    if not non_recursive:
        non_recursive = ['e']  # Add epsilon
    
    # Find a new nonterminal name
    new_nonterminal = get_new_nonterminal(used_nonterminals)
    used_nonterminals.add(new_nonterminal)
    
    # Create new productions
    # A -> β₁A' | β₂A' | ... | βₙA'
    new_A_productions = []
    for beta in non_recursive:
        new_A_productions.append(beta + new_nonterminal)
    
    # A' -> α₁A' | α₂A' | ... | αₘA' | ε
    new_prime_productions = []
    for alpha in recursive:
        new_prime_productions.append(alpha + new_nonterminal)
    new_prime_productions.append('e')  # Add epsilon
    
    result = {
        nonterminal: new_A_productions,
        new_nonterminal: new_prime_productions
    }
    
    return result, used_nonterminals


def get_new_nonterminal(used_nonterminals):
    """
    Find an unused uppercase letter for a new nonterminal.
    Priority: Z, Y, X, W, V, U, T, R, Q, P, O, N, M, L, K, J, I, H, G, F, E, D, C, B
    (Avoiding A and S which are commonly used)
    """
    # Start from Z and go backwards
    for char in 'ZYXWVUTRQPONMLKJIHGFEDCB':
        if char not in used_nonterminals:
            return char
    
    # If all letters are used (very unlikely), use double letters
    for c1 in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        for c2 in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            candidate = c1 + c2
            if candidate not in used_nonterminals:
                return candidate
    
    raise Exception("No available nonterminal names")


def substitute_productions(target_nt, source_nt, source_productions, target_production):
    """
    Substitute a nonterminal in a production.
    
    If target_production is "Aⱼγ", replace it with "δ₁γ | δ₂γ | ... | δₖγ"
    where Aⱼ -> δ₁ | δ₂ | ... | δₖ
    
    Returns: list of new productions
    """
    # Check if production starts with source_nt
    if not target_production or target_production[0] != source_nt:
        return [target_production]
    
    # Get γ (everything after source_nt)
    gamma = target_production[1:]
    
    # Create new productions by substituting
    new_productions = []
    for delta in source_productions:
        new_productions.append(delta + gamma)
    
    return new_productions


def eliminate_left_recursion(grammar):
    """
    Implement Algorithm 4.19 to eliminate all left recursion.
    
    Input: Grammar G with no cycles or ε-productions
    Output: Equivalent grammar with no left recursion
    """
    # Step 1: Arrange nonterminals in some order A₁, A₂, ..., Aₙ
    # We'll use alphabetical order, with S first if present
    nonterminals = list(grammar.keys())
    if 'S' in nonterminals:
        nonterminals.remove('S')
        nonterminals.sort()
        nonterminals = ['S'] + nonterminals
    else:
        nonterminals.sort()
    
    # Keep track of used nonterminals (including new ones we create)
    used_nonterminals = set(nonterminals)
    
    # Step 2: for each i from 1 to n
    n = len(nonterminals)
    for i in range(n):
        A_i = nonterminals[i]
        
        # Step 3: for each j from 1 to i-1
        for j in range(i):
            A_j = nonterminals[j]
            
            # Step 4: Replace each production of the form A_i -> A_j γ
            new_productions = []
            for production in grammar[A_i]:
                if production and production[0] == A_j:
                    # Substitute A_j with its productions
                    substituted = substitute_productions(A_j, A_j, grammar[A_j], production)
                    new_productions.extend(substituted)
                else:
                    new_productions.append(production)
            
            grammar[A_i] = new_productions
        
        # Step 6: Eliminate immediate left recursion among A_i-productions
        if has_immediate_left_recursion(A_i, grammar[A_i]):
            new_grammar, used_nonterminals = eliminate_immediate_left_recursion(
                A_i, grammar[A_i], used_nonterminals
            )
            # Update grammar with new productions
            grammar.update(new_grammar)
    
    return grammar


def format_output(grammar):
    """
    Format grammar for output.
    Follow the same format as input: <nonterminal> -> <productions separated by spaces>
    """
    # Output in order: original nonterminals first (S first if exists), then new ones
    output_lines = []
    
    # Separate original and new nonterminals
    original_nts = []
    new_nts = []
    
    for nt in grammar.keys():
        if len(nt) == 1 and nt in 'SABCDEFGHIJKLMNOPQRTUVWXYZ':
            if nt == 'S':
                original_nts.insert(0, nt)
            else:
                original_nts.append(nt)
        else:
            new_nts.append(nt)
    
    # Sort new nonterminals
    new_nts.sort()
    
    # Combine and output
    all_nts = original_nts + new_nts
    
    for nt in all_nts:
        if nt in grammar:
            productions = ' '.join(grammar[nt])
            output_lines.append(f"{nt} -> {productions}")
    
    return '\n'.join(output_lines)


def main():
    """Main function to process input and output results"""
    import sys
    
    # Check if input is from a file (non-interactive) or terminal (interactive)
    is_interactive = sys.stdin.isatty()
    
    if is_interactive:
        print("=== Left Recursion Elimination Algorithm ===")
        print("Based on Aho et al. 2006, Section 4.3.3\n")
    
    # Read number of cases
    if is_interactive:
        print("Enter the number of test cases:")
    n = int(input().strip())
    
    results = []
    
    for case_num in range(n):
        if is_interactive:
            print(f"\n--- Case {case_num + 1} ---")
            print(f"Enter the number of nonterminals:")
        
        # Read number of nonterminals
        k = int(input().strip())
        
        if is_interactive:
            print(f"Enter {k} production rule(s) in format: <NONTERMINAL> -> <production1> <production2> ...")
            print("Example: S -> Sa b")
        
        # Read k lines of productions
        lines = []
        for i in range(k):
            if is_interactive:
                print(f"  Production {i + 1}: ", end='')
            lines.append(input().strip())
        
        # Parse grammar
        grammar = parse_grammar(lines)
        
        # Eliminate left recursion
        result_grammar = eliminate_left_recursion(grammar)
        
        # Format output
        output = format_output(result_grammar)
        results.append(output)
    
    # Print results
    if is_interactive:
        print("\n" + "="*50)
        print("RESULTS")
        print("="*50 + "\n")
    
    # Print all results with blank line between cases
    print('\n\n'.join(results))


if __name__ == "__main__":
    main()