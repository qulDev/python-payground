#!/usr/bin/env python3
"""
GitHub Contribution Graph Enhancer
Script untuk mempercantik GitHub contribution graph dengan commits yang dapat dikustomisasi
"""

import os
import subprocess
import random
from datetime import datetime, timedelta
import json

class GitHubContributionEnhancer:
    def __init__(self, repo_path="./github-contributions"):
        self.repo_path = repo_path
        self.config_file = "contribution_config.json"
        
    def create_config(self):
        """Membuat file konfigurasi default"""
        config = {
            "start_date": "2024-01-01",
            "end_date": "2024-12-31",
            "min_commits_per_day": 1,
            "max_commits_per_day": 10,
            "skip_weekends": False,
            "commit_patterns": [
                "Fixed bug in module",
                "Updated documentation",
                "Refactored code",
                "Added new feature",
                "Improved performance",
                "Updated dependencies",
                "Fixed typo",
                "Code cleanup",
                "Added tests",
                "Updated README"
            ]
        }
        
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=4)
        print(f"✅ File konfigurasi dibuat: {self.config_file}")
        print("📝 Edit file ini untuk mengatur periode dan jumlah commits")
        
    def load_config(self):
        """Memuat konfigurasi dari file"""
        if not os.path.exists(self.config_file):
            print("⚠️  File konfigurasi tidak ditemukan. Membuat yang baru...")
            self.create_config()
            return None
            
        with open(self.config_file, 'r') as f:
            config = json.load(f)
        return config
    
    def setup_repository(self):
        """Membuat dan setup repository lokal"""
        # Konversi ke absolute path
        abs_repo_path = os.path.abspath(self.repo_path)
        
        if os.path.exists(abs_repo_path):
            print(f"📁 Repository sudah ada di: {abs_repo_path}")
            # Update self.repo_path ke absolute path
            self.repo_path = abs_repo_path
            return
            
        os.makedirs(abs_repo_path)
        self.repo_path = abs_repo_path
        os.chdir(self.repo_path)
        
        # Initialize git repository
        subprocess.run(['git', 'init'], check=True)
        
        # Check and set git config
        self.check_git_config()
        
        # Create initial file
        with open('README.md', 'w') as f:
            f.write("# GitHub Contributions\n\nRepository untuk meningkatkan contribution graph.\n")
            
        subprocess.run(['git', 'add', 'README.md'], check=True)
        subprocess.run(['git', 'commit', '-m', 'Initial commit'], check=True)
        
        print(f"✅ Repository dibuat di: {self.repo_path}")
    
    def check_git_config(self):
        """Cek dan setup git config yang benar"""
        try:
            # Cek email saat ini
            current_email = subprocess.run(['git', 'config', 'user.email'], 
                                         capture_output=True, text=True).stdout.strip()
            current_name = subprocess.run(['git', 'config', 'user.name'], 
                                        capture_output=True, text=True).stdout.strip()
            
            print(f"📧 Git email saat ini: {current_email}")
            print(f"👤 Git name saat ini: {current_name}")
            
            if not current_email:
                print("⚠️  Git email belum di-set!")
                email = input("Masukkan email GitHub Anda: ").strip()
                subprocess.run(['git', 'config', '--global', 'user.email', email], check=True)
                
            if not current_name:
                print("⚠️  Git username belum di-set!")
                name = input("Masukkan username GitHub Anda: ").strip()
                subprocess.run(['git', 'config', '--global', 'user.name', name], check=True)
                
            # Konfirmasi email
            final_email = subprocess.run(['git', 'config', 'user.email'], 
                                       capture_output=True, text=True).stdout.strip()
            
            print(f"✅ Menggunakan email: {final_email}")
            print("⚠️  PENTING: Pastikan email ini sama dengan email di akun GitHub Anda!")
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Error checking git config: {e}")
    
    def verify_github_settings(self):
        """Memberikan checklist untuk memastikan contributions terlihat"""
        print("\n🔍 CHECKLIST AGAR CONTRIBUTIONS TERLIHAT:")
        print("=" * 50)
        print("✅ 1. Email git sama dengan email GitHub account")
        print("✅ 2. Repository bersifat PUBLIC")
        print("✅ 3. Commits di default branch (main/master)")
        print("✅ 4. GitHub Profile Settings:")
        print("   - Private contributions: ON (jika repo private)")
        print("   - Activity overview: ON")
        print("✅ 5. Tunggu beberapa menit untuk sinkronisasi")
        print("\n💡 Jika masih tidak muncul:")
        print("   - Cek https://github.com/settings/profile")
        print("   - Pastikan email verified di GitHub")
        print("   - Repository tidak di-fork")
        
    def create_commit(self, date, commit_message):
        """Membuat commit dengan tanggal tertentu"""
        # Format tanggal untuk git
        date_str = date.strftime("%Y-%m-%d 12:00:00")
        
        # Buat perubahan kecil pada file
        filename = "contributions.txt"
        with open(filename, 'a') as f:
            f.write(f"{date_str}: {commit_message}\n")
            
        subprocess.run(['git', 'add', filename], check=True)
        
        # Set environment variables untuk tanggal commit
        env = os.environ.copy()
        env['GIT_AUTHOR_DATE'] = date_str
        env['GIT_COMMITTER_DATE'] = date_str
        
        subprocess.run(['git', 'commit', '-m', commit_message], 
                      env=env, check=True)
        
    def generate_contributions(self):
        """Generate contributions berdasarkan konfigurasi"""
        config = self.load_config()
        if not config:
            return
            
        # Parse tanggal
        start_date = datetime.strptime(config['start_date'], "%Y-%m-%d")
        end_date = datetime.strptime(config['end_date'], "%Y-%m-%d")
        
        # Simpan path saat ini
        original_path = os.getcwd()
        
        # Setup repository
        self.setup_repository()
        
        # Pastikan kita di directory yang benar
        if not os.path.exists(self.repo_path):
            print(f"❌ Error: Directory {self.repo_path} tidak ditemukan!")
            return
            
        os.chdir(os.path.abspath(self.repo_path))
        
        print(f"🚀 Mulai generate contributions dari {start_date.date()} sampai {end_date.date()}")
        
        current_date = start_date
        total_commits = 0
        
        try:
            while current_date <= end_date:
                # Skip weekend jika diatur
                if config.get('skip_weekends', False) and current_date.weekday() >= 5:
                    current_date += timedelta(days=1)
                    continue
                
                # Tentukan jumlah commits untuk hari ini
                min_commits = config['min_commits_per_day']
                max_commits = config['max_commits_per_day']
                num_commits = random.randint(min_commits, max_commits)
                
                # Buat commits
                for i in range(num_commits):
                    commit_message = random.choice(config['commit_patterns'])
                    if num_commits > 1:
                        commit_message += f" ({i+1})"
                    
                    self.create_commit(current_date, commit_message)
                    total_commits += 1
                
                print(f"📅 {current_date.date()}: {num_commits} commits")
                current_date += timedelta(days=1)
                
        except Exception as e:
            print(f"❌ Error: {e}")
        finally:
            os.chdir(original_path)
            
        print(f"✅ Selesai! Total {total_commits} commits dibuat")
        print(f"📍 Repository location: {os.path.abspath(self.repo_path)}")
        
    def setup_remote(self, remote_url):
        """Setup remote repository"""
        original_path = os.getcwd()
        
        # Pastikan repository path ada
        if not os.path.exists(self.repo_path):
            print(f"❌ Repository tidak ditemukan di: {self.repo_path}")
            print("💡 Jalankan 'Generate contributions' terlebih dahulu")
            return
            
        os.chdir(os.path.abspath(self.repo_path))
        
        try:
            # Cek apakah remote sudah ada
            result = subprocess.run(['git', 'remote', 'get-url', 'origin'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print(f"⚠️  Remote origin sudah ada: {result.stdout.strip()}")
                replace = input("Ganti dengan URL baru? (y/n): ").lower().strip()
                if replace == 'y':
                    subprocess.run(['git', 'remote', 'set-url', 'origin', remote_url], check=True)
                    print(f"✅ Remote origin diupdate: {remote_url}")
                return
            
            subprocess.run(['git', 'remote', 'add', 'origin', remote_url], check=True)
            print(f"✅ Remote origin ditambahkan: {remote_url}")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error setup remote: {e}")
        finally:
            os.chdir(original_path)
            
    def push_to_github(self, branch='main'):
        """Push ke GitHub"""
        original_path = os.getcwd()
        
        # Pastikan repository path ada
        if not os.path.exists(self.repo_path):
            print(f"❌ Repository tidak ditemukan di: {self.repo_path}")
            print("💡 Jalankan 'Generate contributions' terlebih dahulu")
            return
            
        os.chdir(os.path.abspath(self.repo_path))
        
        try:
            # Cek apakah ada remote origin
            result = subprocess.run(['git', 'remote', 'get-url', 'origin'], 
                                  capture_output=True, text=True)
            if result.returncode != 0:
                print("❌ Remote origin belum di-setup!")
                print("💡 Jalankan 'Setup remote GitHub' terlebih dahulu")
                return
            
            # Rename master ke main jika perlu
            subprocess.run(['git', 'branch', '-M', branch], check=True)
            
            # Push ke GitHub
            print(f"📤 Pushing ke branch '{branch}'...")
            try:
                subprocess.run(['git', 'push', '-u', 'origin', branch], check=True)
                print("✅ Berhasil push ke GitHub!")
                print("🎉 Cek contribution graph Anda di GitHub!")
                print(f"🔗 Repository: {result.stdout.strip()}")
            except subprocess.CalledProcessError:
                print("⚠️  Push ditolak karena ada conflict dengan remote repository")
                print("\nPilihan untuk mengatasi:")
                print("1. Force push (HATI-HATI: akan menimpa history GitHub)")
                print("2. Pull dulu kemudian push")
                print("3. Batal")
                
                choice = input("Pilih (1/2/3): ").strip()
                
                if choice == '1':
                    confirm = input("⚠️  YAKIN ingin force push? Ini akan menghapus history GitHub (y/n): ")
                    if confirm.lower() == 'y':
                        subprocess.run(['git', 'push', '--force', 'origin', branch], check=True)
                        print("✅ Force push berhasil!")
                        print("🎉 Cek contribution graph Anda di GitHub!")
                    else:
                        print("❌ Force push dibatalkan")
                        
                elif choice == '2':
                    try:
                        print("📥 Melakukan pull dari GitHub...")
                        subprocess.run(['git', 'pull', 'origin', branch, '--allow-unrelated-histories'], check=True)
                        print("📤 Mencoba push lagi...")
                        subprocess.run(['git', 'push', '-u', 'origin', branch], check=True)
                        print("✅ Berhasil push setelah merge!")
                        print("🎉 Cek contribution graph Anda di GitHub!")
                    except subprocess.CalledProcessError as e:
                        print(f"❌ Error saat pull/push: {e}")
                        print("💡 Coba opsi force push atau buat repository GitHub baru")
                        
                else:
                    print("❌ Push dibatalkan")
                    
        except subprocess.CalledProcessError as e:
            print(f"❌ Error saat push: {e}")
            print("💡 Pastikan:")
            print("   1. Remote URL sudah benar")
            print("   2. Anda sudah login ke GitHub")
            print("   3. Repository sudah dibuat di GitHub")
        finally:
            os.chdir(original_path)

def main():
    enhancer = GitHubContributionEnhancer()
    
    print("🎨 GitHub Contribution Graph Enhancer")
    print("=" * 40)
    
    while True:
        print("\nPilihan:")
        print("1. Buat/Edit konfigurasi")
        print("2. Generate contributions")
        print("3. Setup remote GitHub")
        print("4. Push ke GitHub")
        print("5. Cek GitHub settings")
        print("6. Keluar")
        
        choice = input("\nPilih opsi (1-6): ").strip()
        
        if choice == '1':
            enhancer.create_config()
            print("\n📋 Edit file 'contribution_config.json' untuk mengatur:")
            print("   • start_date: Tanggal mulai (YYYY-MM-DD)")
            print("   • end_date: Tanggal selesai (YYYY-MM-DD)")
            print("   • min_commits_per_day: Minimum commits per hari")
            print("   • max_commits_per_day: Maximum commits per hari")
            print("   • skip_weekends: true/false untuk skip weekend")
            
        elif choice == '2':
            enhancer.generate_contributions()
            
        elif choice == '3':
            remote_url = input("Masukkan URL repository GitHub: ").strip()
            if remote_url:
                enhancer.setup_remote(remote_url)
            else:
                print("❌ URL tidak boleh kosong")
                
        elif choice == '4':
            branch = input("Branch name (default: main): ").strip() or 'main'
            enhancer.push_to_github(branch)
            
        elif choice == '5':
            enhancer.verify_github_settings()
            
        elif choice == '6':
            print("👋 Selamat tinggal!")
            break
            
        else:
            print("❌ Pilihan tidak valid")

if __name__ == "__main__":
    main()