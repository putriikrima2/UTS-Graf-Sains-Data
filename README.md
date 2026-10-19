# UTS Graf Sains Data — Analisis RetailRocket

## Deskripsi Proyek

Repository ini berisi hasil pengerjaan Ujian Tengah Semester (UTS) mata kuliah Graf Sains Data menggunakan dataset RetailRocket. Analisis dilakukan untuk membangun representasi graf interaksi pengguna dan item, menghitung kemiripan antar-pengguna menggunakan Cosine Similarity, serta menghasilkan rekomendasi item menggunakan metode K-Nearest Neighbors (KNN).

## Dataset

Dataset yang digunakan adalah RetailRocket, yang memuat aktivitas pengunjung pada platform e-commerce, termasuk:

- `view` — aktivitas melihat item.
- `addtocart` — aktivitas menambahkan item ke keranjang.
- `transaction` — aktivitas pembelian.

Analisis menggunakan dua periode data, yaitu P1 (6 Mei–4 Juni 2015) dan P2 (2–15 September 2015).

## Metode Analisis

1. **Persiapan data:** Membersihkan dan memfilter data interaksi pengguna serta item.
2. **Pembentukan graf:** Merepresentasikan pengguna sebagai node `Visitor`, item sebagai node `Item`, dan aktivitas sebagai relationship `VIEWED`, `ADDED_TO_CART`, serta `BOUGHT` menggunakan Neo4j.
3. **Vector Space Model (VSM):** Membentuk representasi User–Item dan memvisualisasikan graf pengguna maupun item.
4. **Cosine Similarity:** Mengukur tingkat kemiripan pola interaksi antar-pengguna dan menyimpannya melalui relationship `SIMILAR_TO`.
5. **KNN:** Menghasilkan rekomendasi item berdasarkan kemiripan pengguna.
6. **Evaluasi:** Menggunakan metrik Hit@5 dan NDCG@5.

## Ringkasan Hasil

- Graf VSM User terdiri atas 30 node dan 371 hubungan similarity positif.
- Graf VSM Item terdiri atas 30 node dan 204 edge.
- User `286616` digunakan sebagai acuan visualisasi Cosine Similarity.
- User `163561` memiliki nilai similarity tertinggi terhadap user acuan, yaitu sekitar 0,1463.
- Evaluasi KNN menghasilkan Hit@5 = 0 dan NDCG@5 = 0 pada skenario pengujian yang digunakan.

## Isi Repository

- `UTS_Graf_Sains_Data (3).ipynb` — notebook analisis, kode Python, query Cypher, visualisasi, dan interpretasi.
- Dataset dan file hasil pengolahan — data yang digunakan dalam analisis.

## Teknologi

Python, Google Colab, Pandas, NumPy, Scikit-learn, NetworkX, Matplotlib, dan Neo4j.

## Catatan

Hasil analisis, query Cypher, dan visualisasi dapat dilihat pada notebook. Data RetailRocket digunakan untuk keperluan pembelajaran dan analisis graf.
