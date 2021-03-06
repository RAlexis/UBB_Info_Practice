package Model.Expression;

import Model.Utils.IDictionary;
import Model.Utils.ISymTable;
import Model.Utils.MyDictionary;
import Model.Utils.MyHeap;

public class VarExp implements IExpression {
    private String name;

    public VarExp(String name) {
        this.name = name;
    }

    @Override
    public int evaluate(IDictionary<String, Integer> symTable, MyHeap<Integer> heap) {
        if (symTable.contains(this.name)) {
            return symTable.get(this.name);
        } else {
            throw new RuntimeException("Non existent variable");
        }
    }

    @Override
    public String toString() {
        return this.name;
    }
}
