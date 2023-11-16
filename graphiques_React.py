import React, { useEffect, useState } from 'react';
import { Bar } from 'react-chartjs-2';

const Graphique = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        fetch('https://127.0.0.1/collecte')
            .then(response => response.json())
            .then(data => setData(data));
    }, []);

    const chartData = {
        labels: data.map(collecte => collecte.categorie_socioprofessionnelle),
        datasets: [{
            label: 'Dépenses par catégorie',
            data: data.map(collecte => collecte.depense),
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
        }]
    };

    return <Bar data={chartData} />;
};

export default Graphique;
