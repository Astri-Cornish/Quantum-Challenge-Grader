
import random

from typeguard import typechecked
from typing import Callable

from networkx.classes import Graph
from numpy import ndarray

from qiskit import QuantumCircuit
from qiskit.algorithms.minimum_eigen_solvers.vqe import VQEResult
from qiskit.opflow.primitive_ops.pauli_sum_op import PauliSumOp
from qiskit.primitives import SamplerResult
from qiskit.result import ProbDistribution, QuasiDistribution

from qc_grader.grader.grade import grade
from qc_grader.grader.common import (
    graph_to_json,
    circuit_to_json,
    vqeresult_to_json,
    samplerresult_to_json,
    probdistribution_to_json
)

_challenge_id = 'fall_2022'


@typechecked
def grade_lab3_ex1(attempt_graph: Graph, attempt_n: int) -> None:
    answer = {
        'attempt_n': attempt_n,
        'attempt_graph': graph_to_json(attempt_graph)
    }
    grade(answer, 'ex3-1', _challenge_id)

@typechecked
def grade_lab3_ex2(attempt_ising: PauliSumOp) -> None:
    grade(attempt_ising, 'ex3-2', _challenge_id)


@typechecked
def grade_lab3_ex3(attempt_qc: QuantumCircuit) -> None:
    grade(attempt_qc, 'ex3-3', _challenge_id)


@typechecked
def grade_lab3_ex4(attempt: QuasiDistribution) -> None:
    grade(attempt, 'ex3-4', _challenge_id)


@typechecked
def grade_lab3_ex5(attempt_etgl: Callable) -> None:
    n = random.randint(2, 4)
    qc = attempt_etgl(n)
    answer = {
        'input': n,
        'output': circuit_to_json(qc)
    }
    grade(answer, 'ex3-5', _challenge_id)


@typechecked
def grade_lab3_ex6(result: VQEResult) -> None:
    grade(result, 'ex3-6', _challenge_id)


@typechecked
def grade_lab3_ex7(
    sampler_result: SamplerResult,
    result_prob_dist: ProbDistribution
) -> None:
    answer = {
        'sampler_result': samplerresult_to_json(sampler_result),
        'result_prob_dist': probdistribution_to_json(result_prob_dist)
    }
    grade(answer, 'ex3-7', _challenge_id) 


@typechecked
def grade_lab3_ex8(model_3: QuantumCircuit, result_m3: VQEResult) -> None:
    answer = {
        'qc': circuit_to_json(model_3),
        'vqeresult': vqeresult_to_json(result_m3)
    }
    grade(answer, 'ex3-8', _challenge_id)


@typechecked
def grade_lab3_ex9(vqe_result: VQEResult, bitstring: ndarray) -> None:
    answer = {
        'vqe_result': vqeresult_to_json(vqe_result),
        'bitstring': bitstring
    }
    status, _ = grade(answer, 'ex3-9', _challenge_id, return_response=True)
    if status:
        print("""
Congratulations!
You've successfully carved a clear path for your slingshot by targeting and collecting 
certain orbiting objects with your drones.

You are almost ready to perform your slingshot. As you move your starship into position,
you wonder curiously about the other you out there.

Have they ceased to exist now that you haven't followed their path by selecting this planet?
Do they somehow exist in an alternate reality?

You can never know.

Nonetheless, you look out the window at the planets you didn't select, and whisper an aching,
heartfelt, "Thank you."
        """)
