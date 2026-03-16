import React, { useState, useEffect } from 'react';
import axios from 'axios';

const API_BASE = process.env.REACT_APP_API_URL || 'http://localhost:8080';

function App() {
  const [health, setHealth] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    checkHealth();
    const interval = setInterval(checkHealth, 30000);
    return () => clearInterval(interval);
  }, []);

  const checkHealth = async () => {
    try {
      const response = await axios.get(`${API_BASE}/api/v1/health`);
      setHealth(response.data);
      setError(null);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div style={styles.container}>
        <h1>SmartReplenish</h1>
        <p>Загрузка...</p>
      </div>
    );
  }

  return (
    <div style={styles.container}>
      <header style={styles.header}>
        <h1>📦 SmartReplenish</h1>
        <p style={styles.subtitle}>Система интеллектуального прогнозирования и оптимизации запасов</p>
      </header>

      <div style={styles.status}>
        <h2>Статус системы</h2>
        {error ? (
          <div style={styles.error}>Ошибка: {error}</div>
        ) : (
          <div style={styles.healthGrid}>
            <div style={styles.statusCard}>
              <span style={styles.statusLabel}>Общий статус:</span>
              <span style={{
                ...styles.statusValue,
                color: health?.status === 'healthy' ? '#00ff88' : '#ffb800'
              }}>
                {health?.status === 'healthy' ? '● В норме' : '● Деgraded'}
              </span>
            </div>
            
            {health?.services && Object.entries(health.services).map(([name, service]) => (
              <div key={name} style={styles.serviceCard}>
                <span style={styles.serviceName}>{name}</span>
                <span style={{
                  ...styles.serviceStatus,
                  color: service.status === 'healthy' ? '#00ff88' : '#ff4560'
                }}>
                  {service.status === 'healthy' ? '● OK' : '● ERROR'}
                </span>
                {service.latency_ms && (
                  <span style={styles.latency}>{service.latency_ms.toFixed(1)} ms</span>
                )}
              </div>
            ))}
          </div>
        )}
      </div>

      <div style={styles.links}>
        <h2>Быстрые ссылки</h2>
        <div style={styles.linkGrid}>
          <a href="/api/v1/docs" style={styles.link} target="_blank" rel="noopener noreferrer">
            📚 API Документация
          </a>
          <a href="http://localhost:3030" style={styles.link} target="_blank" rel="noopener noreferrer">
            📊 Grafana Dashboards
          </a>
          <a href="http://localhost:9090" style={styles.link} target="_blank" rel="noopener noreferrer">
            📈 Prometheus Metrics
          </a>
          <a href="http://localhost:8123" style={styles.link} target="_blank" rel="noopener noreferrer">
            💾 ClickHouse
          </a>
        </div>
      </div>

      <footer style={styles.footer}>
        <p>SmartReplenish v1.0.0 | © 2026 SmartReplenish Team</p>
      </footer>
    </div>
  );
}

const styles = {
  container: {
    minHeight: '100vh',
    backgroundColor: '#060810',
    color: '#e8edf5',
    fontFamily: "'IBM Plex Mono', monospace",
    padding: '20px',
  },
  header: {
    textAlign: 'center',
    padding: '40px 0',
    borderBottom: '1px solid #1e2d45',
    marginBottom: '40px',
  },
  subtitle: {
    color: '#4a5568',
    marginTop: '10px',
  },
  status: {
    maxWidth: '800px',
    margin: '0 auto 40px',
  },
  healthGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
    gap: '16px',
    marginTop: '20px',
  },
  statusCard: {
    backgroundColor: '#0d1117',
    border: '1px solid #1e2d45',
    borderRadius: '12px',
    padding: '20px',
    gridColumn: '1 / -1',
  },
  statusLabel: {
    display: 'block',
    fontSize: '12px',
    color: '#4a5568',
    marginBottom: '8px',
  },
  statusValue: {
    fontSize: '24px',
    fontWeight: 'bold',
  },
  serviceCard: {
    backgroundColor: '#0d1117',
    border: '1px solid #1e2d45',
    borderRadius: '8px',
    padding: '16px',
    display: 'flex',
    flexDirection: 'column',
    gap: '8px',
  },
  serviceName: {
    fontSize: '14px',
    textTransform: 'uppercase',
    letterSpacing: '1px',
  },
  serviceStatus: {
    fontSize: '12px',
  },
  latency: {
    fontSize: '11px',
    color: '#4a5568',
  },
  error: {
    backgroundColor: 'rgba(255, 69, 96, 0.1)',
    border: '1px solid #ff4560',
    borderRadius: '8px',
    padding: '16px',
    color: '#ff4560',
  },
  links: {
    maxWidth: '800px',
    margin: '0 auto 40px',
  },
  linkGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))',
    gap: '16px',
    marginTop: '20px',
  },
  link: {
    backgroundColor: '#0d1117',
    border: '1px solid #1e2d45',
    borderRadius: '8px',
    padding: '16px',
    color: '#00e5ff',
    textDecoration: 'none',
    textAlign: 'center',
    transition: 'all 0.2s',
  },
  footer: {
    textAlign: 'center',
    padding: '40px 0',
    borderTop: '1px solid #1e2d45',
    color: '#4a5568',
    fontSize: '12px',
  },
};

export default App;
