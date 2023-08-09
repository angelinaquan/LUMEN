package edu.stanford.cs.crypto;

import cyclops.collections.immutable.VectorX;
import edu.stanford.cs.crypto.efficientct.GeneratorParams;
import edu.stanford.cs.crypto.efficientct.util.ProofUtils;
import edu.stanford.cs.crypto.efficientct.VerificationFailedException;
import edu.stanford.cs.crypto.efficientct.commitments.PeddersenCommitment;
import edu.stanford.cs.crypto.efficientct.linearalgebra.GeneratorVector;
import edu.stanford.cs.crypto.efficientct.multirangeproof.MultiRangeProofProver;
import edu.stanford.cs.crypto.efficientct.multirangeproof.MultiRangeProofSystem;
import edu.stanford.cs.crypto.efficientct.multirangeproof.MultiRangeProofVerifier;
import edu.stanford.cs.crypto.efficientct.rangeproof.RangeProof;
import org.openjdk.jmh.annotations.*;

@State(Scope.Benchmark)
public class MultiProofBenchmark {
    private final MultiRangeProofSystem rangeProofSystem = new MultiRangeProofSystem();
    private final MultiRangeProofProver prover = new MultiRangeProofProver();
    private final GeneratorParams generatorParams = GeneratorParams.generateParams(1024);
    private GeneratorVector commitments;
    private VectorX<PeddersenCommitment> witness;
    private RangeProof oneProof;
    private MultiRangeProofVerifier verifier = new MultiRangeProofVerifier();

    @Setup
    public void setUp() {
        witness = VectorX.generate(6, () -> ProofUtils.randomNumber(60)).map(x -> new PeddersenCommitment(generatorParams.getBase(), x)).materialize();


        commitments = GeneratorVector.from(witness.map(PeddersenCommitment::getCommitment));
        oneProof = testProving();
    }

    @Benchmark
    @BenchmarkMode(Mode.AverageTime)
    public RangeProof testProving() {
        return prover.generateProof(generatorParams, commitments, witness);
        // This is a demo/sample template for building your JMH benchmarks. Edit as needed.
        // Put your benchmark code here.
    }

    @Benchmark
    @BenchmarkMode(Mode.AverageTime)
    public void testVerifying() throws VerificationFailedException {
        verifier.verify(generatorParams, commitments, oneProof);
        // This is a demo/sample template for building your JMH benchmarks. Edit as needed.
        // Put your benchmark code here.
    }


}
