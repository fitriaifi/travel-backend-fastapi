from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict
import uvicorn
import re

app = FastAPI(title="Travel Recommendation AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database Destinasi (tetap sama)
DESTINATIONS = [
    # ... (data destinations tetap sama) ...
]

# AI KEYWORDS MAPPING
AI_KEYWORDS = {
    # KOTA
    "bandung": ["bandung", "ciwidey", "lembang", "cikole", "braga"],
    "jakarta": ["jakarta", "dki", "monas", "kota tua", "taman mini"],
    "yogyakarta": ["yogyakarta", "jogja", "borobudur", "prambanan", "malioboro"],
    "surabaya": ["surabaya", "jawa timur", "tugu pahlawan", "kenjeran"],
    "makassar": ["makassar", "sulawesi", "losari", "rotterdam", "malino"],
    "bali": ["bali", "kuta", "ubud", "seminyak", "denpasar"],
    
    # KATEGORI
    "wisata alam": ["alam", "pegunungan", "kawah", "air terjun", "taman"],
    "wisata sejarah": ["sejarah", "museum", "candi", "benteng", "heritage"],
    "wisata kuliner": ["kuliner", "makan", "restoran", "seafood", "kafe"],
    "wisata keluarga": ["keluarga", "anak", "taman bermain", "zoo", "edukasi"],
    "wisata pantai": ["pantai", "beach", "surfing", "sunset", "laut"],
    "spot foto": ["foto", "instagramable", "fotografi", "indah", "pemandangan"],
    "tempat romantis": ["romantis", "couple", "pasangan", "sunset", "malam"],
    "harga murah": ["murah", "murah meriah", "low budget", "hemat", "gratis"],
    "tempat hits": ["hits", "viral", "trending", "populer", "terkenal"],
}

@app.get("/")
def root():
    return {"message": "AI Travel Recommendation API", "status": "running"}

@app.get("/destinations")
def get_destinations():
    return {"success": True, "destinations": DESTINATIONS}

@app.post("/ai-recommend")
async def ai_recommendation(request: dict):
    """AI-powered travel recommendation"""
    try:
        query = request.get("query", "").lower().strip()
        
        if not query:
            return {"success": True, "destinations": DESTINATIONS[:8]}
        
        print(f"🤖 AI Processing: '{query}'")
        
        # ANALISIS QUERY DENGAN AI SEDERHANA
        matched_cities = []
        matched_categories = []
        matched_keywords = []
        
        # Cari kota yang disebut
        for city, keywords in AI_KEYWORDS.items():
            if any(keyword in query for keyword in keywords):
                if city in ["bandung", "jakarta", "yogyakarta", "surabaya", "makassar", "bali"]:
                    matched_cities.append(city)
                else:
                    matched_categories.append(city)
        
        # Ekstrak keyword spesifik
        query_words = query.split()
        for word in query_words:
            if len(word) > 3:  # Abaikan kata pendek
                matched_keywords.append(word)
        
        print(f"📍 Cities: {matched_cities}")
        print(f"📂 Categories: {matched_categories}")
        print(f"🔑 Keywords: {matched_keywords}")
        
        # FILTER DESTINASI
        results = []
        
        for dest in DESTINATIONS:
            score = 0
            
            # 1. Priority: Kota yang disebut
            if matched_cities:
                dest_city = dest.get("city", "").lower()
                if dest_city in matched_cities:
                    score += 100
            
            # 2. Priority: Kategori yang disebut
            if matched_categories:
                dest_cats = dest.get("category", [])
                dest_tags = dest.get("tags", [])
                dest_type = dest.get("type", "").lower()
                
                for cat in matched_categories:
                    cat_keywords = AI_KEYWORDS.get(cat, [])
                    # Cek di category
                    if any(cat_kw in ' '.join(dest_cats).lower() for cat_kw in cat_keywords):
                        score += 50
                    # Cek di tags
                    elif any(cat_kw in ' '.join(dest_tags).lower() for cat_kw in cat_keywords):
                        score += 40
                    # Cek di type
                    elif any(cat_kw in dest_type for cat_kw in cat_keywords):
                        score += 30
            
            # 3. Keyword matching
            dest_text = f"{dest.get('name', '')} {dest.get('description', '')} {' '.join(dest.get('tags', []))}"
            dest_text = dest_text.lower()
            
            for keyword in matched_keywords:
                if keyword in dest_text:
                    score += 10
            
            # 4. Jika query langsung match nama/tags
            if query in dest.get("name", "").lower():
                score += 80
            if query in dest.get("city", "").lower():
                score += 70
            
            if score > 0:
                results.append((score, dest))
        
        # Sort by score
        results.sort(key=lambda x: x[0], reverse=True)
        final_results = [dest for score, dest in results]
        
        # Jika tidak ada hasil, cari berdasarkan kota default
        if not final_results and matched_cities:
            city = matched_cities[0]
            for dest in DESTINATIONS:
                if dest.get("city", "").lower() == city:
                    final_results.append(dest)
        
        # Jika masih kosong, return beberapa destinasi populer
        if not final_results:
            final_results = DESTINATIONS[:6]
        
        # Remove duplicates
        seen_ids = set()
        unique_results = []
        for dest in final_results:
            if dest["id"] not in seen_ids:
                seen_ids.add(dest["id"])
                unique_results.append(dest)
        
        return {
            "success": True,
            "destinations": unique_results[:12],
            "query": query,
            "ai_analysis": {
                "detected_cities": matched_cities,
                "detected_categories": matched_categories,
                "keywords": matched_keywords
            },
            "count": len(unique_results)
        }
        
    except Exception as e:
        print(f"❌ AI Error: {str(e)}")
        return {"success": False, "error": str(e)}

@app.post("/search")
async def search_destinations(request: dict):
    """Traditional search (for compatibility)"""
    try:
        query = request.get("query", "").lower().strip()
        
        if not query:
            return {"success": True, "destinations": DESTINATIONS[:8]}
        
        results = []
        
        # Simple search
        for dest in DESTINATIONS:
            # Cek kota
            if query in dest.get("city", "").lower():
                results.append(dest)
                continue
            
            # Cek nama destinasi
            if query in dest.get("name", "").lower():
                results.append(dest)
                continue
            
            # Cek tags
            if any(query in tag.lower() for tag in dest.get("tags", [])):
                results.append(dest)
                continue
        
        # Sort by rating
        results.sort(key=lambda x: x.get("rating", 0), reverse=True)
        
        # Remove duplicates
        seen_ids = set()
        unique_results = []
        for dest in results:
            if dest["id"] not in seen_ids:
                seen_ids.add(dest["id"])
                unique_results.append(dest)
        
        return {
            "success": True,
            "destinations": unique_results[:12],
            "query": query,
            "count": len(unique_results)
        }
        
    except Exception as e:
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)
