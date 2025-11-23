tool_schema = [
    # 1. FILE ORGANIZER
    {
        "type": "function",
        "function": {
            "name": "file_organizer",
            "description": "Merapikan folder dengan mengelompokkan file berdasarkan jenis ekstensi.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Path folder yang ingin dirapikan"
                    }
                },
                "required": ["path"]
            }
        }
    },

    # 2. SYSTEM CHECK RAM
    {
        "type": "function",
        "function": {
            "name": "system_check_ram",
            "description": "Mengecek sisa RAM laptop.",
            "parameters": {
                "type": "object",
                "properties": {}
            },
            "required": []
        }
    },

    # 3. KALKULATOR SUHU
    {
        "type": "function",
        "function": {
            "name": "kalkulator_suhu",
            "description": "Mengkonversi suhu antar Celsius dan Fahrenheit.",
            "parameters": {
                "type": "object",
                "properties": {
                    "nilai": {"type": "number"},
                    "dari": {"type": "string", "description": "C atau F"},
                    "ke": {"type": "string", "description": "C atau F"}
                },
                "required": ["nilai", "dari", "ke"]
            }
        }
    },

    # 4. KALKULATOR DISKON
    {
        "type": "function",
        "function": {
            "name": "kalkulator_diskon",
            "description": "Menghitung harga setelah diskon.",
            "parameters": {
                "type": "object",
                "properties": {
                    "harga": {"type": "number"},
                    "diskon": {"type": "number", "description": "0-100"}
                },
                "required": ["harga", "diskon"]
            }
        }
    },

    # 5. BACA FILE TEKS
    {
        "type": "function",
        "function": {
            "name": "baca_file_teks",
            "description": "Membaca isi file .txt.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"}
                },
                "required": ["path"]
            }
        }
    }

]
