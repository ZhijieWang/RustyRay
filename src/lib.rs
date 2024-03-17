//rustimport
use pyo3::prelude::*;
use pyo3::pyclass;
use pyo3::pymethods;
#[pyclass]
pub struct Prover{
    x: usize
}
#[pymethods]
impl Prover {
    #[new]
    fn new(value : usize)-> Self{
        Prover{ x: value}
    }
    fn prove_txn(&mut self, a: usize)-> usize{
        self.x = self.x + a;
        return self.x;
    }
}

// #[pyfunction]
// fn proove(py: Python) ->PyResult<Int>{
//     Ok(6)
// }

#[pymodule]
#[pyo3(name = "prover")]
fn prover(_py: Python, m: &PyModule) -> PyResult<()> {
    // m.add_wrapped(wrap_pyfunction!(proove))?;
    m.add_class::<Prover>()?;
    Ok(())
}

