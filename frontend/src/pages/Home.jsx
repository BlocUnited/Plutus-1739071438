import React from 'react';
import HeroSection from '../components/HeroSection';
import PortfolioCard from '../components/PortfolioCard';
import { fetchData } from '../utils/api';

/**
 * Home page component.
 * Displays the hero section and featured portfolios.
 */
const Home = () => {
    const [portfolios, setPortfolios] = React.useState([]);
    const [loading, setLoading] = React.useState(true);

    React.useEffect(() => {
        const loadPortfolios = async () => {
            try {
                const data = await fetchData('portfolios');
                setPortfolios(data);
            } catch (error) {
                console.error('Error fetching portfolios:', error);
            } finally {
                setLoading(false);
            }
        };
        loadPortfolios();
    }, []);

    return (
        <div className="home-page">
            <HeroSection
                image="http://example.com/hero.jpg"
                title="Welcome to Our Platform"
                description="Explore amazing portfolios and connect with mentors!"
            />
            <div className="portfolio-grid">
                {loading ? (
                    <p>Loading portfolios...</p>
                ) : (
                    portfolios.map(portfolio => (
                        <PortfolioCard
                            key={portfolio.id}
                            title={portfolio.title}
                            image={portfolio.media[0]?.url}
                            description={portfolio.description}
                        />
                    ))
                )}
            </div>
        </div>
    );
};

export default Home;
