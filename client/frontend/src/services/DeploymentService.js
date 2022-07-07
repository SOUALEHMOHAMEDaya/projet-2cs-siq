const API_URL = "http://127.0.0.1:8000/run-deployment";

export const runDeployment = async (deployment) => {
    const res = await fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(deployment),
    });

    return await res.json();

}