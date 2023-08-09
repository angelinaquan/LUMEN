package edu.stanford.cs.crypto;

import edu.stanford.cs.crypto.efficientct.VerificationFailedException;
import edu.stanford.cs.crypto.efficientct.innerproduct.*;
import edu.stanford.cs.crypto.efficientct.linearalgebra.FieldVector;
import edu.stanford.cs.crypto.efficientct.linearalgebra.VectorBase;
import org.bouncycastle.math.ec.ECPoint;
import org.openjdk.jmh.annotations.*;

@State(Scope.Benchmark)
public class InnerProductBenchmark {
    private final InnerProductProofSystem rangeProofSystem = new InnerProductProofSystem();
    private final InnerProductProver prover = new InnerProductProver();
    private final VectorBase generatorParams = rangeProofSystem.generatePublicParams(1024);
    private ECPoint commitment;
    private InnerProductWitness witness;
    private InnerProductProof oneProof;
    private EfficientInnerProductVerifier verifier1 = new EfficientInnerProductVerifier();
    private InnerProductVerifier verifier2 = new InnerProductVerifier();

    @Setup
    public void setUp() {
        FieldVector as = FieldVector.random(1024);
        FieldVector bs = FieldVector.random(1024);
        witness = new InnerProductWitness(as, bs);
        commitment = generatorParams.commit(as, bs, as.innerPoduct(bs));
        oneProof = testProving();
    }

    @Benchmark
    @BenchmarkMode(Mode.AverageTime)
    public InnerProductProof testProving() {
        return prover.generateProof(generatorParams, commitment, witness);
        // This is a demo/sample template for building your JMH benchmarks. Edit as needed.
        // Put your benchmark code here.
    }

    @Benchmark
    @BenchmarkMode(Mode.AverageTime)
    public void testVerifying1() throws VerificationFailedException {
        verifier1.verify(generatorParams, commitment, oneProof);
        // This is a demo/sample template for building your JMH benchmarks. Edit as needed.
        // Put your benchmark code here.
    }
    @Benchmark
    @BenchmarkMode(Mode.AverageTime)
    public void testVerifying2() throws VerificationFailedException {
        verifier2.verify(generatorParams, commitment, oneProof);
        // This is a demo/sample template for building your JMH benchmarks. Edit as needed.
        // Put your benchmark code here.
    }

}
