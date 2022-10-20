
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
from qc_grader.grader.common import graph_to_json, circuit_to_json


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
    grade(sampler_result, result_prob_dist, 'ex3-7', _challenge_id) 


@typechecked
def grade_lab3_ex8(model_3: QuantumCircuit, result_m3: VQEResult) -> None:
    grade(model_3, result_m3, 'ex3-8', _challenge_id) 


@typechecked
def grade_lab3_ex9(vqe_result: VQEResult, bitstring: ndarray) -> None:
    grade(vqe_result, bitstring, 'ex3-9', _challenge_id) 
