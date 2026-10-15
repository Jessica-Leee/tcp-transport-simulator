# TCP Transport Simulator

A course implementation of a **TCP subset** for **UC Berkeley CS 168, Spring 2026, Project 3: Transport**, running inside the supplied POX-based network simulator. It **does not implement congestion control** and is not a production TCP stack.

## Implementation

The submitted implementation is `ext/cs168p2/student_socket.py`, built on the course's socket skeleton. It includes active connection establishment, ordered byte-stream reception with an out-of-order queue, acknowledgments and sliding windows, connection teardown, timeout retransmission, and RTT-based retransmission-timeout updates.

The implementation does not support passive server-side `LISTEN`/`SYN_RECEIVED` behavior. RFC references in the source describe partial implementations, not complete compliance.

## Repository map

| Location | Purpose |
| --- | --- |
| [`ext/cs168p2/student_socket.py`](ext/cs168p2/student_socket.py) | Recovered final submission, including the course-provided socket interface. |
| [`ext/cs168p2/tests/`](ext/cs168p2/tests/), [`ext/cs168p2/autograder.py`](ext/cs168p2/autograder.py) | Course scenarios and test harness. |
| [`ext/tcpip/`](ext/tcpip/), [`pox/`](pox/) | Supplied simulated network stack and POX framework. |
| [`run_tests.py`](run_tests.py) | Local test entry point with consistent interpreter selection. |
| [Checks](CHECKS.txt), [source notices](THIRD_PARTY.md) | Verification scope, final-submission hash, and framework provenance. |

## Run the simulated tests

Use **Python 3.12** from an existing installation. This archive was verified with Python **3.12.6**. No pip packages, native capture extension, or external network access are required for the course simulation tests.

From the repository root:

```sh
python3.12 run_tests.py all
```

Run one stage or one test:

```sh
python3.12 run_tests.py s8
python3.12 run_tests.py s1_t1
```

Use the full path to your Python 3.12 executable if it is not named `python3.12`. The helper runs the supplied autograder and tests without changing their logic, uses the same interpreter for simulation subprocesses, and returns a failing exit code when tests fail. Test runs create ignored `ext/cs168p2/trace/` captures.

The original course entry point is `ext/cs168p2/autograder.py`. Its `pox.py` launcher searches `PATH` for `python3`; the helper avoids accidentally mixing Python versions. Python 3.13+ and the optional real-network modes have not been validated here.

## Verification

- The complete supplied autograder passed: **30 tests across 9 stages**, using Python 3.12.6.
- Syntax checks passed for all retained Python source files. Two warnings occur in untouched, unrelated POX modules; see `CHECKS.txt`.
- The recovered final submission was copied byte for byte. No transport algorithm was changed during packaging.

Submission SHA-256:

```text
1dfae1e87aa7519ec831afe577c58555aec09a92039f2b0d4872c841190bbcfa
```

These results describe the supplied tests, not complete TCP/RFC coverage. Detailed checks and limits are in `CHECKS.txt`.

The results were recorded during archive preparation on **October 14, 2026**. No simulations were rerun for this documentation refresh. Generated traces and captures are runtime output, not required repository inputs.

## Framework and source attribution

The network simulator, reference socket code, packet utilities, test harness, and test scenarios are supplied course/framework material, not claimed as original student work. The original upstream README is preserved as `docs/UPSTREAM_README.md`; existing source copyright and license notices are retained.

Sources: [official Spring 2026 starter archive](https://sp26.cs168.io/assets/projects/proj3/cs168-sp26-proj3-transport.zip) and [POX upstream](https://github.com/noxrepo/pox). See `THIRD_PARTY.md` for provenance and licensing notes.

Packaging omits caches, captures, traces, Git/IDE metadata, the downloaded ZIP, and optional browser GUI/download/documentation tooling. It adds this README, ignore rules, a test launcher, and verification notes. The headless simulator and course test fixtures remain intact.

## Private course archive

Keep this repository **private** under the course's solution-sharing policy. It is prepared for private review and preservation, not public distribution. No new open-source license is applied to course or student materials.
