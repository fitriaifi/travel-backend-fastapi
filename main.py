from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict
import uvicorn

app = FastAPI(title="Travel Recommendation AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database Destinasi Indonesia dengan gambar spesifik
DESTINATIONS = [
    # ===== BANDUNG =====
    {
        "id": 1,
        "name": "Kawah Putih Ciwidey",
        "category": ["nature", "mountain", "photography"],
        "type": "Wisata Alam",
        "region": "jawa",
        "city": "Bandung",
        "price": "low",
        "description": "Danau kawah vulkanik dengan air berwarna putih kebiruan yang menakjubkan di ketinggian 2.430 mdpl.",
        "image": "https://images.unsplash.com/photo-1597074866923-dc0589150358?w=800&auto=format&fit=crop",
        "tags": ["Alam", "Kawah", "Fotografi", "Pegunungan", "Ciwidey"],
        "best_for": ["Keluarga", "Fotografi", "Petualangan"],
        "province": "Jawa Barat",
        "rating": 4.5,
        "attractions": ["Danau Kawah Putih", "View Point", "Kawasan Wisata", "Spot Foto"],
        "best_time": "Pagi hari (07:00-11:00)",
        "entrance_fee": "Rp 25.000 - Rp 50.000"
    },
    {
        "id": 2,
        "name": "Dusun Bambu",
        "category": ["family", "nature", "culinary"],
        "type": "Wisata Keluarga",
        "region": "jawa",
        "city": "Bandung",
        "price": "medium",
        "description": "Wisata alam dengan konsep eco-park, rumah pohon, dan kuliner khas Sunda di kawasan Lembang.",
        "image": "https://images.unsplash.com/photo-1548013146-72479768bada?w=800&auto=format&fit=crop",
        "tags": ["Keluarga", "Alam", "Kuliner", "Eco Park", "Lembang"],
        "best_for": ["Keluarga", "Romantis", "Kuliner"],
        "province": "Jawa Barat",
        "rating": 4.4,
        "attractions": ["Rumah Pohon", "Kolam Ikan", "Resto Apung", "Taman Bunga"],
        "best_time": "Siang dan sore",
        "entrance_fee": "Rp 30.000 - Rp 100.000"
    },
    {
        "id": 3,
        "name": "Lembang Park & Zoo",
        "category": ["family", "animals", "nature"],
        "type": "Kebun Binatang",
        "region": "jawa",
        "city": "Bandung",
        "price": "medium",
        "description": "Kebun binatang modern dengan koleksi satwa lengkap dan wahana permainan di Lembang.",
        "image": "https://images.unsplash.com/photo-1518709268805-4e9042af2176?w=800&auto=format&fit=crop",
        "tags": ["Keluarga", "Hewan", "Wahana", "Edukasi", "Lembang"],
        "best_for": ["Keluarga", "Anak-anak", "Edukasi"],
        "province": "Jawa Barat",
        "rating": 4.3,
        "attractions": ["Koleksi Satwa", "Wahana Permainan", "Show Animals", "Spot Foto"],
        "best_time": "Pagi dan siang",
        "entrance_fee": "Rp 50.000 - Rp 150.000"
    },
    {
        "id": 4,
        "name": "Orchid Forest Cikole",
        "category": ["nature", "flowers", "photography"],
        "type": "Taman Bunga",
        "region": "jawa",
        "city": "Bandung",
        "price": "medium",
        "description": "Hutan anggrek terbesar dengan koleksi ribuan anggrek dan spot foto instagramable di Cikole.",
        "image": "https://images.unsplash.com/photo-1566385101042-1a0f0c126c96?w=800&auto=format&fit=crop",
        "tags": ["Anggrek", "Fotografi", "Alam", "Cikole", "Instagramable"],
        "best_for": ["Fotografi", "Romantis", "Alam"],
        "province": "Jawa Barat",
        "rating": 4.6,
        "attractions": ["Kebun Anggrek", "Jembatan Gantung", "Spot Foto", "Kafe"],
        "best_time": "Pagi dan sore",
        "entrance_fee": "Rp 40.000 - Rp 80.000"
    },
    {
        "id": 5,
        "name": "Jalan Braga",
        "category": ["history", "culinary", "shopping"],
        "type": "Wisata Kota",
        "region": "jawa",
        "city": "Bandung",
        "price": "low",
        "description": "Jalan legendaris Bandung dengan arsitektur kolonial Belanda, kafe, butik, dan galeri seni.",
        "image": "https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=800&auto=format&fit=crop",
        "tags": ["Sejarah", "Kuliner", "Belanja", "Kolonial", "Heritage"],
        "best_for": ["Backpacker", "Kuliner", "Fotografi", "Sejarah"],
        "province": "Jawa Barat",
        "rating": 4.2,
        "attractions": ["Arsitektur Kolonial", "Kafe Tua", "Butik", "Galeri Seni"],
        "best_time": "Siang dan malam",
        "entrance_fee": "Gratis"
    },
    
    # ===== MAKASSAR =====
    {
        "id": 6,
        "name": "Benteng Rotterdam",
        "category": ["history", "culture", "photography"],
        "type": "Benteng Sejarah",
        "region": "sulawesi",
        "city": "Makassar",
        "price": "low",
        "description": "Benteng peninggalan Kerajaan Gowa-Tallo abad ke-16 yang menjadi museum dan ikon sejarah Makassar.",
        "image": "https://images.unsplash.com/photo-1588666309990-d68f08e3d4c6?w=800&auto=format&fit=crop",
        "tags": ["Sejarah", "Benteng", "Museum", "Heritage", "Fotografi"],
        "best_for": ["Sejarah", "Edukasi", "Fotografi", "Keluarga"],
        "province": "Sulawesi Selatan",
        "rating": 4.4,
        "attractions": ["Benteng Utama", "Museum La Galigo", "Menara Pengawas", "Taman"],
        "best_time": "Pagi dan sore",
        "entrance_fee": "Rp 5.000 - Rp 10.000"
    },
    {
        "id": 7,
        "name": "Pantai Losari",
        "category": ["beach", "culinary", "sunset"],
        "type": "Pantai Kota",
        "region": "sulawesi",
        "city": "Makassar",
        "price": "low",
        "description": "Pantai ikonik Makassar sepanjang 1 km terkenal dengan sunset terindah dan kuliner seafood malam hari.",
        "image": "https://images.unsplash.com/photo-1506929562872-bb421503ef21?w=800&auto=format&fit=crop",
        "tags": ["Pantai", "Sunset", "Kuliner", "Seafood", "Iconic"],
        "best_for": ["Keluarga", "Kuliner", "Romantis", "Backpacker"],
        "province": "Sulawesi Selatan",
        "rating": 4.3,
        "attractions": ["Sunset View", "Taman Pantai", "Kuliner Malam", "Pusat Kota"],
        "best_time": "Sore dan malam (sunset)",
        "entrance_fee": "Gratis"
    },
    {
        "id": 8,
        "name": "Trans Studio Makassar",
        "category": ["family", "entertainment", "indoor"],
        "type": "Theme Park",
        "region": "sulawesi",
        "city": "Makassar",
        "price": "high",
        "description": "Taman tema indoor terbesar di Indonesia Timur dengan wahana seru dan pertunjukan spektakuler.",
        "image": "https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=800&auto=format&fit=crop",
        "tags": ["Theme Park", "Wahana", "Keluarga", "Indoor", "Hiburan"],
        "best_for": ["Keluarga", "Anak-anak", "Petualangan"],
        "province": "Sulawesi Selatan",
        "rating": 4.5,
        "attractions": ["Wahana Ekstrem", "Pertunjukan", "Area Kids", "Food Court"],
        "best_time": "Sepanjang hari",
        "entrance_fee": "Rp 200.000 - Rp 350.000"
    },
    {
        "id": 9,
        "name": "Malino Highlands",
        "category": ["nature", "mountain", "cool"],
        "type": "Wisata Pegunungan",
        "region": "sulawesi",
        "city": "Makassar",
        "price": "medium",
        "description": "Kawasan pegunungan dengan udara sejuk, kebun teh, air terjun, dan pemandangan alam menakjubkan.",
        "image": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&auto=format&fit=crop",
        "tags": ["Pegunungan", "Udara Sejuk", "Alam", "Teh", "Malino"],
        "best_for": ["Keluarga", "Petualangan", "Alam", "Romantis"],
        "province": "Sulawesi Selatan",
        "rating": 4.6,
        "attractions": ["Kebun Teh", "Air Terjun", "View Point", "Perkebunan"],
        "best_time": "Pagi dan siang",
        "entrance_fee": "Rp 20.000 - Rp 50.000"
    },
    
    # ===== BALI =====
    {
        "id": 10,
        "name": "Pantai Kuta",
        "category": ["beach", "surfing", "sunset"],
        "type": "Pantai",
        "region": "bali",
        "city": "Bali",
        "price": "low",
        "description": "Pantai terkenal untuk surfing pemula dengan ombak konsisten dan sunset spektakuler.",
        "image": "https://images.unsplash.com/photo-1518548419970-58e3b4079ab2?w=800&auto=format&fit=crop",
        "tags": ["Pantai", "Surfing", "Sunset", "Turis", "Kuta"],
        "best_for": ["Backpacker", "Surfing", "Sunset", "Sosial"],
        "province": "Bali",
        "rating": 4.3,
        "attractions": ["Surfing Spot", "Sunset View", "Beach Walk", "Warung Pantai"],
        "best_time": "Sore (sunset)",
        "entrance_fee": "Gratis"
    },
    
    # ===== YOGYAKARTA =====
    {
        "id": 11,
        "name": "Candi Borobudur",
        "category": ["history", "culture", "unesco"],
        "type": "Candi Budha",
        "region": "jawa",
        "city": "Yogyakarta",
        "price": "medium",
        "description": "Candi Budha terbesar di dunia dari abad ke-9, warisan dunia UNESCO dengan arsitektur megah.",
        "image": "https://images.unsplash.com/photo-1621784567609-b6ba6a5c47d8?w=800&auto=format&fit=crop",
        "tags": ["Candi", "UNESCO", "Sejarah", "Budha", "Magelang"],
        "best_for": ["Sejarah", "Budaya", "Fotografi", "Keluarga"],
        "province": "Jawa Tengah",
        "rating": 4.8,
        "attractions": ["Candi Utama", "Relief Cerita", "Sunrise View", "Museum"],
        "best_time": "Pagi (sunrise)",
        "entrance_fee": "Rp 50.000 - Rp 350.000"
    },
    
    # ===== JAKARTA =====
    {
        "id": 12,
        "name": "Monas (Monumen Nasional)",
        "category": ["history", "landmark", "city"],
        "type": "Monumen",
        "region": "jawa",
        "city": "Jakarta",
        "price": "low",
        "description": "Monumen ikonik setinggi 132 meter dengan museum sejarah Indonesia dan view kota dari puncak.",
        "image": "https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=800&auto=format&fit=crop",
        "tags": ["Monumen", "Sejarah", "Ikon", "Museum", "Landmark"],
        "best_for": ["Keluarga", "Sejarah", "Fotografi", "Backpacker"],
        "province": "DKI Jakarta",
        "rating": 4.2,
        "attractions": ["Puncak Monas", "Museum Sejarah", "Taman", "Air Mancur"],
        "best_time": "Pagi dan sore",
        "entrance_fee": "Rp 5.000 - Rp 20.000"
    },
    
    # ===== SURABAYA =====
    {
        "id": 13,
        "name": "Tugu Pahlawan",
        "category": ["history", "landmark", "city"],
        "type": "Monumen",
        "region": "jawa",
        "city": "Surabaya",
        "price": "low",
        "description": "Monumen perjuangan setinggi 41 meter dengan museum 10 November mengenang Pertempuran Surabaya.",
        "image": "https://images.unsplash.com/photo-1567217250058-0c7e61eb3f5d?w=800&auto=format&fit=crop",
        "tags": ["Monumen", "Sejarah", "Pahlawan", "Museum", "Kota"],
        "best_for": ["Sejarah", "Edukasi", "Keluarga", "Backpacker"],
        "province": "Jawa Timur",
        "rating": 4.1,
        "attractions": ["Monumen", "Museum 10 November", "Taman", "Patung"],
        "best_time": "Pagi dan sore",
        "entrance_fee": "Rp 2.000 - Rp 5.000"
    }
]

# Mapping pencarian
CITY_MAPPING = {
    "bandung": ["Bandung", "Jawa Barat", "Ciwidey", "Lembang", "Cikole", "Braga"],
    "makassar": ["Makassar", "Sulawesi Selatan", "Losari", "Rotterdam", "Malino"],
    "bali": ["Bali", "Kuta", "Ubud", "Seminyak", "Denpasar"],
    "yogyakarta": ["Yogyakarta", "Jogja", "Borobudur", "Prambanan", "Malioboro"],
    "jakarta": ["Jakarta", "DKI", "Monas", "Kota Tua", "Taman Mini"],
    "surabaya": ["Surabaya", "Jawa Timur", "Tugu Pahlawan", "Kenjeran"],
    "medan": ["Medan", "Sumatera Utara", "Maimun", "Rahmat"],
    "semarang": ["Semarang", "Jawa Tengah", "Lawang Sewu"],
    "bogor": ["Bogor", "Jawa Barat", "Kebun Raya", "Puncak"],
    "malang": ["Malang", "Jawa Timur", "Batu", "Selecta"],
}

@app.get("/")
def root():
    return {"message": "Travel Recommendation API - Wisata Spesifik", "status": "running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/destinations")
def get_destinations():
    return {"success": True, "destinations": DESTINATIONS}

@app.post("/search")
def search_destinations(request: Dict):
    """Search destinations by city name"""
    try:
        query = request.get("query", "").lower().strip()
        region = request.get("region", "all")
        
        print(f"🔍 Search query: '{query}', region: '{region}'")
        
        if not query:
            return {"success": True, "destinations": DESTINATIONS[:8]}
        
        results = []
        
        # Cari berdasarkan mapping kota
        if query in CITY_MAPPING:
            search_terms = CITY_MAPPING[query]
            for dest in DESTINATIONS:
                # Cek kota
                if dest.get("city", "").lower() == query:
                    results.append(dest)
                    continue
                
                # Cek berdasarkan search terms
                for term in search_terms:
                    if term.lower() in dest.get("city", "").lower() or \
                       term.lower() in dest.get("name", "").lower() or \
                       term.lower() in dest.get("province", "").lower():
                        results.append(dest)
                        break
        
        # Jika tidak ditemukan via mapping, cari general
        if not results:
            for dest in DESTINATIONS:
                # Cek nama destinasi
                if query in dest["name"].lower():
                    results.append(dest)
                    continue
                
                # Cek kota
                if query in dest.get("city", "").lower():
                    results.append(dest)
                    continue
                
                # Cek tags
                if any(query in tag.lower() for tag in dest.get("tags", [])):
                    results.append(dest)
                    continue
                
                # Cek attractions
                if any(query in attr.lower() for attr in dest.get("attractions", [])):
                    results.append(dest)
                    continue
        
        # Filter by region jika dipilih
        if region != "all":
            results = [dest for dest in results if dest.get("region") == region]
        
        # Remove duplicates
        seen_ids = set()
        unique_results = []
        for dest in results:
            if dest["id"] not in seen_ids:
                seen_ids.add(dest["id"])
                unique_results.append(dest)
        
        # Sort by rating (descending)
        unique_results.sort(key=lambda x: x.get("rating", 0), reverse=True)
        
        print(f"✅ Found {len(unique_results)} destinations for '{query}'")
        
        return {
            "success": True,
            "destinations": unique_results[:15],
            "query": query,
            "count": len(unique_results)
        }
        
    except Exception as e:
        print(f"❌ Search error: {str(e)}")
        return {"success": False, "error": str(e)}

@app.post("/filter")
def filter_by_region(request: Dict):
    """Filter destinations by region"""
    try:
        region = request.get("region", "all")
        
        if region == "all":
            filtered = DESTINATIONS
        else:
            filtered = [dest for dest in DESTINATIONS if dest.get("region") == region]
        
        # Sort by rating
        filtered.sort(key=lambda x: x.get("rating", 0), reverse=True)
        
        return {
            "success": True,
            "destinations": filtered[:12],
            "region": region,
            "count": len(filtered)
        }
        
    except Exception as e:
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    print("🌴 TRAVEL RECOMMENDATION API (WISATA SPESIFIK)")
    print("=" * 60)
    print("🌐 Server URL: http://localhost:8000")
    print("🔍 Search endpoint: POST http://localhost:8000/search")
    print("📍 Filter by region: POST http://localhost:8000/filter")
    print(f"📊 Total Destinasi: {len(DESTINATIONS)} destinasi spesifik")
    print(f"🏙️  Kota tersedia: {', '.join(sorted(CITY_MAPPING.keys()))}")
    print("\n📡 Waiting for search requests...\n")
    
    uvicorn.run(app, host="0.0.0.0", port=8000)