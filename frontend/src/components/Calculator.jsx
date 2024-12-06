import React, { useState } from "react";
import axios from "axios";

const Calculator = ({ token }) => {
    const [num1, setNum1] = useState("");
    const [num2, setNum2] = useState("");
    const [operation, setOperation] = useState("");
    const [result, setResult] = useState("");
    const [error, setError] = useState("");

    const handleCalculation = async () => {
        setError(""); // Limpa erros anteriores
        setResult(""); // Limpa o resultado anterior

        // Validação de entrada
        if (!num1 || !num2 || !operation) {
            setError("Por favor, preencha todos os campos e escolha uma operação.");
            return;
        }

        try {
            const response = await axios.post(
                "http://localhost:8000/calculate",
                {
                    num1: parseFloat(num1),
                    num2: parseFloat(num2),
                    operation,
                },
                {
                    headers: {
                        Authorization: `Bearer ${token}`,
                    },
                }
            );
            setResult(response.data.result);
        } catch (error) {
            setError(
                error.response?.data?.detail || "Erro ao calcular o resultado. Verifique sua conexão ou o token."
            );
        }
    };

    return (
        <div>
            <h2>Calculadora</h2>
            <input
                type="number"
                placeholder="Número 1"
                value={num1}
                onChange={(e) => setNum1(e.target.value)}
            />
            <input
                type="number"
                placeholder="Número 2"
                value={num2}
                onChange={(e) => setNum2(e.target.value)}
            />
            <div>
                <button
                    onClick={() => setOperation("add")}
                    style={{ backgroundColor: operation === "add" ? "#ddd" : "white" }}
                >
                    Somar
                </button>
                <button
                    onClick={() => setOperation("subtract")}
                    style={{ backgroundColor: operation === "subtract" ? "#ddd" : "white" }}
                >
                    Subtrair
                </button>
                <button
                    onClick={() => setOperation("multiply")}
                    style={{ backgroundColor: operation === "multiply" ? "#ddd" : "white" }}
                >
                    Multiplicar
                </button>
                <button
                    onClick={() => setOperation("divide")}
                    style={{ backgroundColor: operation === "divide" ? "#ddd" : "white" }}
                >
                    Dividir
                </button>
            </div>
            <button onClick={handleCalculation}>Calcular</button>
            <div>
                {error && <p style={{ color: "red" }}>{error}</p>}
                {result && <p>Resultado: {result}</p>}
            </div>
        </div>
    );
};

export default Calculator;