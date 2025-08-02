import { use, useEffect, useState } from "react";
import "./App.css";

function App() {
    const [data, setData] = useState([]);

    useEffect(() => {
        fetch("http://localhost:8000/get-top-holding")
            .then((res) => res.json())
            .then((json) => {
                console.log("Fetched: " + data);
                setData(json);
            });
    }, []);

    return (
        <>
            {data.map((item, index) => (
                <div key={index}>
                    <p>
                        {item.stock_code} - {item.industry} -{" "}
                        {item.net_asset_percent}%
                    </p>
                </div>
            ))}
        </>
    );
}

export default App;
