import React, { useState } from "react";
import Login from "./components/Login";
import Calculator from "./components/Calculator";

function App() {
    const [token, setToken] = useState(null); // Estado para armazenar o token JWT

    return (
        <div>
            {!token ? (
                // Exibe a tela de login caso o token não exista
                <Login setToken={setToken} />
            ) : (
                // Exibe a calculadora caso o token exista
                <Calculator token={token} />
            )}
        </div>
    );
}

export default App;