<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🌴 Rekomendasi Liburan AI</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
            color: #333;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        
        /* Header */
        .header {
            text-align: center;
            background: rgba(255, 255, 255, 0.95);
            padding: 40px;
            border-radius: 20px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        }
        
        .header h1 {
            color: #2c3e50;
            font-size: 2.8rem;
            margin-bottom: 10px;
        }
        
        .header p {
            color: #7f8c8d;
            font-size: 1.2rem;
        }
        
        /* Search Section */
        .preferences {
            background: white;
            padding: 40px;
            border-radius: 20px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        }
        
        .preferences h2 {
            text-align: center;
            color: #2c3e50;
            margin-bottom: 30px;
            font-size: 1.8rem;
        }
        
        .search-container {
            max-width: 600px;
            margin: 0 auto 30px;
        }
        
        .search-box {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }
        
        #searchInput {
            flex: 1;
            padding: 15px 20px;
            border: 2px solid #ddd;
            border-radius: 50px;
            font-size: 16px;
            outline: none;
            transition: border-color 0.3s;
            background: #f8f9fa;
        }
        
        #searchInput:focus {
            border-color: #4CAF50;
        }
        
        .search-examples {
            text-align: left;
            background: #f9f9f9;
            padding: 15px;
            border-radius: 10px;
            margin-top: 15px;
        }
        
        .search-examples p {
            margin-bottom: 10px;
            font-weight: bold;
            color: #2c3e50;
        }
        
        .search-example {
            display: inline-block;
            background: white;
            padding: 8px 15px;
            border-radius: 20px;
            border: 1px solid #3498db;
            color: #3498db;
            cursor: pointer;
            font-size: 14px;
            margin-right: 8px;
            margin-bottom: 8px;
            transition: all 0.3s;
        }
        
        .search-example:hover {
            background: #3498db;
            color: white;
            transform: translateY(-2px);
        }
        
        .category-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        
        .category-btn {
            padding: 25px 15px;
            border: 3px solid #e0e0e0;
            border-radius: 15px;
            background: white;
            cursor: pointer;
            font-size: 18px;
            font-weight: 500;
            transition: all 0.3s;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 15px;
        }
        
        .category-btn:hover {
            border-color: #3498db;
            transform: translateY(-5px);
        }
        
        .category-btn.active {
            border-color: #4CAF50;
            background: #e8f5e9;
            color: #2e7d32;
        }
        
        .category-btn i {
            font-size: 2.5rem;
        }
        
        .action-buttons {
            display: flex;
            gap: 20px;
            justify-content: center;
            margin-top: 30px;
        }
        
        .primary-btn, .secondary-btn {
            padding: 18px 40px;
            border: none;
            border-radius: 50px;
            font-size: 18px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }
        
        .primary-btn {
            background: linear-gradient(135deg, #4CAF50, #2E7D32);
            color: white;
            width: 200px;
        }
        
        .primary-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(76, 175, 80, 0.3);
        }
        
        .secondary-btn {
            background: #f5f5f5;
            color: #666;
            width: 200px;
        }
        
        .secondary-btn:hover {
            background: #e0e0e0;
        }
        
        /* Results */
        .results-section {
            background: white;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            min-height: 400px;
        }
        
        .results-section h2 {
            text-align: center;
            color: #2c3e50;
            margin-bottom: 30px;
            font-size: 1.8rem;
        }
        
        .ai-analysis {
            text-align: center;
            background: #e3f2fd;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 20px;
            color: #1976d2;
            font-weight: 500;
        }
        
        .results-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 30px;
        }
        
        .destination-card {
            background: white;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
            transition: all 0.3s;
            border: 1px solid #eee;
            display: flex;
            flex-direction: column;
        }
        
        .destination-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
        }
        
        .destination-image {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }
        
        .destination-content {
            padding: 20px;
            flex-grow: 1;
            display: flex;
            flex-direction: column;
        }
        
        .destination-content h3 {
            font-size: 1.4rem;
            color: #2c3e50;
            margin-bottom: 10px;
        }
        
        .location-badge {
            background: #e3f2fd;
            color: #1976d2;
            padding: 4px 12px;
            border-radius: 15px;
            font-size: 12px;
            font-weight: 600;
            display: inline-block;
            margin-bottom: 10px;
        }
        
        .destination-content p {
            color: #666;
            line-height: 1.6;
            margin-bottom: 15px;
            font-size: 14px;
            flex-grow: 1;
        }
        
        .destination-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-bottom: 15px;
        }
        
        .tag {
            background: #f0f7ff;
            color: #1976d2;
            padding: 4px 10px;
            border-radius: 12px;
            font-size: 11px;
            font-weight: 500;
        }
        
        .destination-meta {
            display: flex;
            justify-content: space-between;
            align-items: center;
            color: #7f8c8d;
            font-size: 13px;
            margin-top: auto;
            padding-top: 15px;
            border-top: 1px solid #eee;
        }
        
        .price-tag {
            background: #e8f5e9;
            color: #2e7d32;
            padding: 4px 12px;
            border-radius: 15px;
            font-weight: 600;
            font-size: 12px;
        }
        
        .rating {
            color: #ff9800;
            font-weight: 600;
            font-size: 13px;
        }
        
        .attraction-count {
            color: #666;
            font-size: 12px;
        }
        
        .no-results {
            text-align: center;
            padding: 60px 20px;
            grid-column: 1/-1;
        }
        
        .no-results i {
            font-size: 3rem;
            color: #7f8c8d;
            margin-bottom: 20px;
        }
        
        /* Loading */
        .loading-container {
            text-align: center;
            padding: 60px 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 300px;
        }
        
        .loading-spinner {
            width: 70px;
            height: 70px;
            border: 5px solid rgba(102, 126, 234, 0.2);
            border-top: 5px solid #667eea;
            border-radius: 50%;
            animation: spin 1.5s ease-in-out infinite;
            margin-bottom: 25px;
        }
        
        .loading-text {
            color: #2c3e50;
            font-size: 1.2rem;
            font-weight: 500;
            margin-bottom: 10px;
        }
        
        .loading-subtext {
            color: #7f8c8d;
            font-size: 0.9rem;
        }
        
        .loading-dots {
            display: flex;
            gap: 8px;
            margin-top: 20px;
        }
        
        .dot {
            width: 12px;
            height: 12px;
            background: #667eea;
            border-radius: 50%;
            animation: dots 1.4s ease-in-out infinite;
        }
        
        .dot:nth-child(2) {
            animation-delay: 0.2s;
        }
        
        .dot:nth-child(3) {
            animation-delay: 0.4s;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        @keyframes dots {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-15px); }
        }
        
        /* Footer */
        .footer {
            text-align: center;
            color: white;
            padding: 30px;
            margin-top: 50px;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 15px;
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            .category-grid {
                grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
            }
            
            .search-box {
                flex-direction: column;
            }
            
            .action-buttons {
                flex-direction: column;
                align-items: center;
            }
            
            .primary-btn, .secondary-btn {
                width: 100%;
                max-width: 300px;
            }
            
            .results-grid {
                grid-template-columns: 1fr;
            }
            
            .destination-image {
                height: 180px;
            }
            
            .header h1 {
                font-size: 2rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Header -->
        <header class="header">
            <h1><i class="fas fa-palm-tree"></i> Rekomendasi Wisata AI</h1>
            <p>Cari destinasi dengan bahasa natural. Contoh: "destinasi wisata Bandung" atau "tempat makan di Jakarta"</p>
        </header>

        <!-- Search Section -->
        <section class="preferences">
            <h2><i class="fas fa-robot"></i> Rekomendasi AI Cerdas</h2>
            
            <div class="search-container">
                <div class="search-box">
                    <input type="text" 
                           id="searchInput" 
                           placeholder="🔍 Tulis permintaan Anda (contoh: destinasi wisata Bandung, tempat romantis Bali, spot foto alam...)">
                    <button class="primary-btn" id="searchBtn">
                        <i class="fas fa-search"></i> Cari AI
                    </button>
                </div>
                
                <div class="search-examples">
                    <p><i class="fas fa-lightbulb"></i> Contoh pencarian AI:</p>
                    <div>
                        <span class="search-example" onclick="setSearch('destinasi wisata Bandung')">destinasi wisata Bandung</span>
                        <span class="search-example" onclick="setSearch('tempat makan di Jakarta')">tempat makan Jakarta</span>
                        <span class="search-example" onclick="setSearch('spot foto alam')">spot foto alam</span>
                        <span class="search-example" onclick="setSearch('wisata keluarga murah')">wisata keluarga murah</span>
                        <span class="search-example" onclick="setSearch('pantai romantis sunset')">pantai romantis</span>
                        <span class="search-example" onclick="setSearch('tempat sejarah Yogyakarta')">sejarah Yogyakarta</span>
                    </div>
                </div>
            </div>
            
            <div class="category-grid" id="categories">
                <button class="category-btn active" data-category="all">
                    <i class="fas fa-globe"></i>
                    🌍 Semua Kota
                </button>
                <button class="category-btn" data-category="jawa">
                    <i class="fas fa-mountain"></i>
                    🏝️ Pulau Jawa
                </button>
                <button class="category-btn" data-category="bali">
                    <i class="fas fa-umbrella-beach"></i>
                    🏖️ Bali & NTB
                </button>
                <button class="category-btn" data-category="sumatera">
                    <i class="fas fa-leaf"></i>
                    🌴 Sumatera
                </button>
                <button class="category-btn" data-category="sulawesi">
                    <i class="fas fa-water"></i>
                    🏞️ Sulawesi
                </button>
            </div>
            
            <div class="action-buttons">
                <button class="secondary-btn" id="resetBtn">
                    <i class="fas fa-redo"></i> Reset Pencarian
                </button>
            </div>
        </section>

        <!-- Results Section -->
        <section class="results-section" id="resultsSection">
            <h2><i class="fas fa-map-marked-alt"></i> Rekomendasi AI</h2>
            
            <div id="aiAnalysis" class="ai-analysis" style="display: none;">
                <!-- AI Analysis akan muncul di sini -->
            </div>
            
            <!-- Loading State -->
            <div id="loading" class="loading-container" style="display: none;">
                <div class="loading-spinner"></div>
                <div class="loading-text">AI sedang menganalisis permintaan Anda...</div>
                <div class="loading-subtext">Mencari rekomendasi terbaik</div>
                <div class="loading-dots">
                    <div class="dot"></div>
                    <div class="dot"></div>
                    <div class="dot"></div>
                </div>
            </div>
            
            <div id="results" class="results-grid">
                <!-- Results will appear here -->
            </div>
        </section>

        <!-- Footer -->
        <footer class="footer">
            <p><i class="fas fa-brain"></i> Rekomendasi Wisata AI • Powered by AI Intelligence</p>
            <p style="opacity: 0.8; margin-top: 10px; font-size: 0.9rem;">
                Sistem AI memahami bahasa natural Anda untuk memberikan rekomendasi terbaik
            </p>
        </footer>
    </div>

<script>
    // GANTI DENGAN URL BACKEND RENDER ANDA
    const BACKEND_URL = 'https://travel-backend-fastapi.onrender.com';
    let selectedRegion = 'all';
    
    // Initialize
    document.addEventListener('DOMContentLoaded', function() {
        console.log('🤖 AI Travel Recommendation Loaded');
        console.log('🌐 Backend URL:', BACKEND_URL);
        setupEventListeners();
        loadAllDestinations();
    });
    
    function setupEventListeners() {
        // Region buttons
        document.querySelectorAll('.category-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                const region = this.getAttribute('data-category');
                selectRegion(region, this);
            });
        });
        
        // Search button
        document.getElementById('searchBtn').addEventListener('click', aiSearchDestinations);
        
        // Enter key pada input search
        document.getElementById('searchInput').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                aiSearchDestinations();
            }
        });
        
        // Reset button
        document.getElementById('resetBtn').addEventListener('click', resetSearch);
    }
    
    function selectRegion(region, button) {
        // Remove active class dari semua buttons
        document.querySelectorAll('.category-btn').forEach(btn => {
            btn.classList.remove('active');
        });
        
        // Add active class ke button yang diklik
        button.classList.add('active');
        selectedRegion = region;
        
        console.log('📍 Region selected:', region);
        
        // Jika region bukan 'all', filter destinasi
        if (region !== 'all') {
            filterByRegion(region);
        } else {
            loadAllDestinations();
        }
    }
    
    function setSearch(query) {
        document.getElementById('searchInput').value = query;
        aiSearchDestinations();
    }
    
    // FUNGSI AI SEARCH YANG BARU
    async function aiSearchDestinations() {
        const searchQuery = document.getElementById('searchInput').value.trim();
        
        if (!searchQuery) {
            alert('⚠️ Masukkan permintaan Anda! Contoh: "destinasi wisata Bandung"');
            return;
        }
        
        console.log('🤖 AI Processing:', searchQuery);
        
        // Tampilkan loading AI
        showLoading(true, `AI menganalisis: "${searchQuery}"`);
        
        try {
            // GUNAKAN ENDPOINT AI YANG BARU
            const response = await fetch(`${BACKEND_URL}/ai-recommend`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    query: searchQuery,
                    region: selectedRegion
                })
            });
            
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('🤖 AI Response:', data);
        
        if (data.success) {
            // TAMPILKAN AI ANALYSIS
            displayAIAnalysis(data.ai_analysis, searchQuery);
            
            if (data.destinations && data.destinations.length > 0) {
                console.log(`✅ ${data.destinations.length} rekomendasi AI ditemukan`);
                displayDestinations(data.destinations, searchQuery);
                
                // Update judul dengan hasil AI
                const regionNames = {
                    'jawa': 'Pulau Jawa',
                    'bali': 'Bali & Nusa Tenggara',
                    'sumatera': 'Pulau Sumatera',
                    'sulawesi': 'Sulawesi'
                };
                
                let title = `<i class="fas fa-robot"></i> `;
                if (selectedRegion !== 'all') {
                    title += `Rekomendasi di ${regionNames[selectedRegion] || selectedRegion}`;
                } else {
                    title += `Rekomendasi AI untuk "${searchQuery}"`;
                }
                document.querySelector('#resultsSection h2').innerHTML = title;
                
            } else {
                showNoResults(searchQuery);
            }
        } else {
            console.error('❌ AI Error:', data.error);
            // Fallback ke search biasa
            await traditionalSearch(searchQuery);
        }
        } catch (error) {
            console.error('❌ AI Search Error:', error);
            
            // Fallback ke search biasa
            showLoading(true, "AI tidak tersedia, menggunakan pencarian biasa...");
            await traditionalSearch(searchQuery);
        } finally {
            showLoading(false);
        }
    }
    
    // FALLBACK: Traditional Search
    async function traditionalSearch(query) {
        try {
            const response = await fetch(`${BACKEND_URL}/search`, {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ 
                    query: query,
                    region: selectedRegion 
                })
            });
            
            const data = await response.json();
            if (data.success && data.destinations.length > 0) {
                displayDestinations(data.destinations, query);
                document.querySelector('#resultsSection h2').innerHTML = 
                    `<i class="fas fa-search"></i> Hasil Pencarian untuk "${query}"`;
            } else {
                showNoResults(query);
            }
        } catch (e) {
            console.error('❌ All methods failed:', e);
            showNoResults(query);
        }
    }
    
    function displayAIAnalysis(aiData, query) {
        const aiAnalysisEl = document.getElementById('aiAnalysis');
        
        if (aiData && (aiData.detected_cities.length > 0 || aiData.detected_categories.length > 0)) {
            let analysisHTML = '<i class="fas fa-brain"></i> AI Analysis: ';
            
            if (aiData.detected_cities.length > 0) {
                analysisHTML += `<span style="color: #1976d2;">📍 ${aiData.detected_cities.map(c => c.charAt(0).toUpperCase() + c.slice(1)).join(', ')}</span>`;
            }
            
            if (aiData.detected_categories.length > 0) {
                if (aiData.detected_cities.length > 0) analysisHTML += ' | ';
                analysisHTML += `<span style="color: #4CAF50;">📂 ${aiData.detected_categories.join(', ')}</span>`;
            }
            
            if (aiData.keywords && aiData.keywords.length > 0) {
                analysisHTML += ` | 🔑 Keywords: ${aiData.keywords.slice(0, 3).join(', ')}`;
            }
            
            aiAnalysisEl.innerHTML = analysisHTML;
            aiAnalysisEl.style.display = 'block';
        } else {
            aiAnalysisEl.style.display = 'none';
        }
    }
    
    async function filterByRegion(region) {
        console.log('🗺️ Filtering by region:', region);
        showLoading(true, `Memfilter destinasi di ${getRegionName(region)}...`);
        
        try {
            const response = await fetch(`${BACKEND_URL}/filter`, {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ region: region })
            });
            
            const data = await response.json();
            if (data.success) {
                displayDestinations(data.destinations);
                
                // Update judul
                document.querySelector('#resultsSection h2').innerHTML = 
                    `<i class="fas fa-map-marked-alt"></i> Destinasi di ${getRegionName(region)}`;
                    
                // Hide AI analysis
                document.getElementById('aiAnalysis').style.display = 'none';
            }
        } catch (error) {
            console.error('Error filtering:', error);
        } finally {
            showLoading(false);
        }
    }
    
    async function loadAllDestinations() {
        showLoading(true, "Memuat semua destinasi wisata...");
        try {
            const response = await fetch(`${BACKEND_URL}/destinations`);
            if (response.ok) {
                const data = await response.json();
                if (data.success) {
                    displayDestinations(data.destinations);
                    document.querySelector('#resultsSection h2').innerHTML = 
                        `<i class="fas fa-map-marked-alt"></i> Semua Destinasi Wisata`;
                    document.getElementById('aiAnalysis').style.display = 'none';
                }
            }
        } catch (error) {
            console.error('Error loading:', error);
        } finally {
            showLoading(false);
        }
    }
    
    function displayDestinations(destinations, searchQuery = '') {
        const resultsEl = document.getElementById('results');
        
        if (!destinations || destinations.length === 0) {
            showNoResults(searchQuery);
            return;
        }
        
        resultsEl.innerHTML = destinations.map(dest => `
            <div class="destination-card">
                <img src="${dest.image}" 
                     alt="${dest.name}" 
                     class="destination-image"
                     onerror="this.onerror=null; this.src='https://images.unsplash.com/photo-1518548419970-58e3b4079ab2?w=800&auto=format&fit=crop';">
                <div class="destination-content">
                    <h3>${dest.name}</h3>
                    <span class="location-badge">${dest.city || dest.province || ''}</span>
                    
                    <div class="destination-tags">
                        ${dest.tags ? dest.tags.slice(0, 4).map(tag => 
                            `<span class="tag">${tag}</span>`
                        ).join('') : ''}
                    </div>
                    
                    <p>${dest.description}</p>
                    
                    <div class="destination-meta">
                        <span class="price-tag">${getPriceText(dest.price)}</span>
                        ${dest.rating ? `<span class="rating">⭐ ${dest.rating}/5</span>` : ''}
                        ${dest.attractions ? `<span class="attraction-count">🏞️ ${dest.attractions.length}+ spot</span>` : ''}
                    </div>
                </div>
            </div>
        `).join('');
        
        // Scroll to results
        document.getElementById('resultsSection').scrollIntoView({behavior: 'smooth'});
    }
    
    function showNoResults(query) {
        const resultsEl = document.getElementById('results');
        resultsEl.innerHTML = `
            <div class="no-results">
                <i class="fas fa-search"></i>
                <h3 style="color: #2c3e50; margin-bottom: 10px;">Tidak ditemukan</h3>
                <p style="color: #666;">Tidak ada rekomendasi untuk "${query}"</p>
                <p style="color: #999; font-size: 0.9rem; margin-top: 10px;">
                    Coba gunakan contoh: "destinasi wisata Bandung", "tempat makan Jakarta", atau "spot foto alam"
                </p>
            </div>
        `;
        document.getElementById('aiAnalysis').style.display = 'none';
    }
    
    function getPriceText(price) {
        const prices = {
            low: '💰 Murah', 
            medium: '💰💰 Sedang', 
            high: '💰💰💰 Mahal'
        };
        return prices[price] || price;
    }
    
    function getRegionName(region) {
        const regions = {
            'all': 'Semua Kota',
            'jawa': 'Pulau Jawa',
            'bali': 'Bali & Nusa Tenggara',
            'sumatera': 'Pulau Sumatera',
            'sulawesi': 'Sulawesi'
        };
        return regions[region] || region;
    }
    
    function showLoading(show, message = "AI sedang menganalisis...") {
        const loadingEl = document.getElementById('loading');
        const resultsEl = document.getElementById('results');
        
        if (show) {
            loadingEl.style.display = 'flex';
            resultsEl.style.display = 'none';
            
            // Update message
            if (message) {
                const loadingText = loadingEl.querySelector('.loading-text');
                if (loadingText) {
                    loadingText.textContent = message;
                }
            }
        } else {
            loadingEl.style.display = 'none';
            resultsEl.style.display = 'grid';
        }
    }
    
    function resetSearch() {
        console.log('🔄 Reset pencarian');
        document.getElementById('searchInput').value = '';
        selectedRegion = 'all';
        
        // Reset semua button region
        document.querySelectorAll('.category-btn').forEach(btn => {
            btn.classList.remove('active');
        });
        
        // Aktifkan button "Semua"
        document.querySelector('.category-btn[data-category="all"]').classList.add('active');
        
        // Hide AI analysis
        document.getElementById('aiAnalysis').style.display = 'none';
        
        loadAllDestinations();
    }
</script>
</body>
</html>
