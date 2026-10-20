
# UTS Graf Sains Data

Repository ini berisi hasil pengerjaan Ujian Tengah Semester (UTS) mata kuliah Graf Sains Data menggunakan dataset RetailRocket. Pengolahan data dilakukan menggunakan Python melalui Jupyter Notebook di VS Code dan database Neo4j untuk membentuk serta menganalisis graf interaksi pengguna dan produk.

## Dataset

Dataset yang digunakan adalah RetailRocket, yaitu data interaksi pengguna dengan produk pada platform e-commerce. Data dibagi menjadi dua periode:

- **P1 (Training):** 6 Mei – 4 Juni 2015, sebanyak 627.860 interaksi.
- **P2 (Testing):** 2 – 15 September 2015, sebanyak 262.381 interaksi.

## Metode dan Analisis

Tahapan pengerjaan meliputi:

1. **Data Wrangling:** Melakukan filter dataset berdasarkan timestamp untuk memperoleh data P1 dan P2.
2. **Pembentukan Graf:** Mengimpor data P1 ke Neo4j untuk membentuk hubungan antara Visitor dan Item.
3. **Vector Space Modelling (VSM):** Membentuk matriks User–Item dan Item–User.
4. **Proyeksi Graf:** Membandingkan proyeksi User–User dan Item–Item menggunakan NetworkX.
5. **Cosine Similarity:** Menghitung kemiripan antarproduk dan menyimpan hasil hubungan similarity di Neo4j.
6. **K-Nearest Neighbors (KNN):** Menghasilkan rekomendasi produk berdasarkan interaksi pengguna.
7. **Evaluasi:** Mengukur hasil rekomendasi menggunakan Hit@5 dan NDCG@5.

## Struktur Repository

```text
UTS-Graf-Sains-Data/
├── UTS_Graf_Sains_Data.ipynb
├── README.md
└── data/
    ├── events.csv
    ├── events_p1.csv
    └── events_p2.csv
```

## Tools yang Digunakan

- Python
- Visual Studio Code
- Jupyter Notebook
- Neo4j
- Pandas
- NumPy
- SciPy
- NetworkX
- Scikit-learn

## Hasil Analisis

Data training P1 menghasilkan graf dengan 325.964 simpul Visitor dan 118.508 simpul Item. Analisis dilanjutkan menggunakan pendekatan Item-Based KNN dengan nilai k = 5 untuk menghasilkan rekomendasi produk.

Evaluasi dilakukan menggunakan data testing P2 dengan metrik Hit@5 dan NDCG@5. Pada pengguna yang dipilih, kedua metrik menghasilkan nilai 0 karena tidak terdapat kecocokan antara lima rekomendasi teratas dengan produk yang diinteraksikan pada periode P2.

Seluruh kode, hasil perhitungan, visualisasi, dan penjelasan terdapat pada notebook `UTS_Graf_Sains_Data.ipynb`.
