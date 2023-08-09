package edu.stanford.cs.crypto.efficientct;

import java.io.Serializable;

public interface Proof extends Serializable {
    byte[] serialize();

}
