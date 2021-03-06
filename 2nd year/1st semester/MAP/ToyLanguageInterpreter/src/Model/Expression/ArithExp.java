package Model.Expression;

import Model.Utils.IDictionary;
import Model.Utils.ISymTable;
import Model.Utils.MyDictionary;
import Model.Utils.MyHeap;

public class ArithExp implements IExpression {
    private IExpression op1, op2;
    private char operator;

    public ArithExp(IExpression op1, char operator, IExpression op2) {
        this.op1 = op1;
        this.op2 = op2;
        this.operator = operator;
    }

    @Override
    public int evaluate(IDictionary<String, Integer> symTable, MyHeap<Integer> heap) {
        int firstRes = this.op1.evaluate(symTable, heap);
        int secondRes = this.op2.evaluate(symTable, heap);

        switch (this.operator) {
            case '+':
                return firstRes + secondRes;

            case '-':
                return firstRes - secondRes;

            case '*':
                return firstRes * secondRes;

            case '/':
                if (secondRes == 0) {
                    throw new RuntimeException("Second operand cannot be 0!");
                }

                return firstRes / secondRes;

            default:
                throw new RuntimeException("Invalid operation entered!");
        }
    }

    @Override
    public String toString() {
        return this.op1.toString() + " " + this.operator + " " + this.op2.toString();
    }
}
