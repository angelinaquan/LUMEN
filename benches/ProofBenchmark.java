package edu.stanford.cs.crypto;

import edu.stanford.cs.crypto.efficientct.GeneratorParams;
import edu.stanford.cs.crypto.efficientct.util.ProofUtils;
import edu.stanford.cs.crypto.efficientct.VerificationFailedException;
import edu.stanford.cs.crypto.efficientct.commitments.PeddersenCommitment;
import edu.stanford.cs.crypto.efficientct.rangeproof.*;
import org.bouncycastle.math.ec.ECPoint;
import org.openjdk.jmh.annotations.*;

import java.math.BigInteger;

@State(Scope.Benchmark)
public class ProofBenchmark {
    private final RangeProofSystem rangeProofSystem = new RangeProofSystem();
    private final RangeProofProver prover = new RangeProofProver();
    private final GeneratorParams generatorParams = GeneratorParams.generateParams(64);
    private ECPoint commitment;
    private PeddersenCommitment witness;
    private RangeProof oneProof;
    private RangeProofVerifier verifier = new RangeProofVerifier();

    @Setup
    public void setUp() {
        BigInteger number = ProofUtils.randomNumber(60);
        this.witness = new PeddersenCommitment(generatorParams.getBase(), number);
        commitment = witness.getCommitment();
        oneProof = testProving();
    }

    @Benchmark
    @BenchmarkMode(Mode.AverageTime)
    public RangeProof testProving() {
        return prover.generateProof(generatorParams, commitment, witness);
        // This is a demo/sample template for building your JMH benchmarks. Edit as needed.
        // Put your benchmark code here.
    }

    @Benchmark
    @BenchmarkMode(Mode.AverageTime)
    public void testVerifying() throws VerificationFailedException {
        verifier.verify(generatorParams, commitment, oneProof);
        // This is a demo/sample template for building your JMH benchmarks. Edit as needed.
        // Put your benchmark code here.
    }

}
