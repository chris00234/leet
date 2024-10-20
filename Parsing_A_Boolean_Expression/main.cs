public class Solution {
    private int pos;
    private string expr;

    public bool ParseBoolExpr(string expression) {
        pos = 0;
        expr = expression;
        return Parse();
    }

    private bool TryEat(char c) {
        if (pos < expr.Length && expr[pos] == c) {
            pos++;
            return true;
        }
        return false;
    }

    private bool Parse() {
        // Parse boolean literals
        if (TryEat('t')) return true;
        if (TryEat('f')) return false;

        // Parse NOT operation
        if (TryEat('!')) {
            pos++; // Skip '('
            bool inner = Parse();
            pos++; // Skip ')'
            return !inner;
        }

        // Parse AND operation
        if (TryEat('&')) {
            pos++; // Skip '('
            bool result = true;
            while (true) {
                result &= Parse();
                if (!TryEat(',')) break;
            }
            pos++; // Skip ')'
            return result;
        }

        // Parse OR operation
        if (TryEat('|')) {
            pos++; // Skip '('
            bool result = false;
            while (true) {
                result |= Parse();
                if (!TryEat(',')) break;
            }
            pos++; // Skip ')'
            return result;
        }

        throw new ArgumentException("Unexpected character.");
    }
}

