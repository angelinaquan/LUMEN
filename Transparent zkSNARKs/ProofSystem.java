package edu.stanford.cs.crypto.efficientct;

public interface ProofSystem<PP, PI, W, P, PR extends Prover<PP, PI, W, P>, V extends Verifier<PP, PI, P>> {
    PR getProver();

    V getVerifier();
}
