"""
Automated Batch Runner for MICE Imputation
Runs all 5 batches (100 datasets total) sequentially.

Usage: python run_all_batches.py
Then go grab a coffee ☕
"""
import subprocess
import sys
import time
from pathlib import Path
from datetime import datetime

SCRIPT_DIR = Path(__file__).parent
MAIN_SCRIPT = SCRIPT_DIR / "miceforest_imputation.py"

def update_batch_number(batch_num):
    """Update BATCH_NUMBER in the main script"""
    content = MAIN_SCRIPT.read_text(encoding='utf-8')
    
    # Find and replace BATCH_NUMBER line
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('BATCH_NUMBER = '):
            lines[i] = f'BATCH_NUMBER = {batch_num}  # Change this: 1, 2, 3, 4, or 5'
            break
    
    MAIN_SCRIPT.write_text('\n'.join(lines), encoding='utf-8')
    print(f"  Updated BATCH_NUMBER to {batch_num}")

def run_batch(batch_num):
    """Run a single batch"""
    print(f"\n{'='*70}")
    print(f"STARTING BATCH {batch_num}/5 - Datasets {(batch_num-1)*20+1} to {batch_num*20}")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*70}\n")
    
    # Update the batch number in the script
    update_batch_number(batch_num)
    
    # Run the imputation script
    start_time = time.time()
    result = subprocess.run(
        [sys.executable, str(MAIN_SCRIPT)],
        cwd=str(SCRIPT_DIR),
        capture_output=False  # Show output in real-time
    )
    
    elapsed = time.time() - start_time
    
    if result.returncode == 0:
        print(f"\n✅ Batch {batch_num} completed in {elapsed/60:.1f} minutes")
        return True
    else:
        print(f"\n❌ Batch {batch_num} FAILED (exit code: {result.returncode})")
        return False

def main():
    print("="*70)
    print("AUTOMATED MICE IMPUTATION - ALL BATCHES")
    print("="*70)
    print(f"Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("This will create 100 imputed datasets in 5 batches of 20")
    print("Go grab a coffee ☕ - this may take a while!")
    print("="*70)
    
    total_start = time.time()
    successful_batches = []
    failed_batches = []
    
    for batch_num in range(1, 6):
        success = run_batch(batch_num)
        if success:
            successful_batches.append(batch_num)
        else:
            failed_batches.append(batch_num)
            print(f"\n⚠️ Batch {batch_num} failed. Continuing with next batch...")
    
    # Final summary
    total_elapsed = time.time() - total_start
    print("\n" + "="*70)
    print("FINAL SUMMARY")
    print("="*70)
    print(f"End time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total time: {total_elapsed/60:.1f} minutes ({total_elapsed/3600:.2f} hours)")
    print(f"\n✅ Successful batches: {successful_batches}")
    if failed_batches:
        print(f"❌ Failed batches: {failed_batches}")
    else:
        print("\n🎉 ALL 100 DATASETS CREATED SUCCESSFULLY!")
        print("You can now run Step 7: Model Development")
    
    # Count files created
    imputed_dir = SCRIPT_DIR / "imputed_data"
    if imputed_dir.exists():
        files = list(imputed_dir.glob("imputed_dataset_*.csv"))
        print(f"\nFiles in imputed_data/: {len(files)}")

if __name__ == "__main__":
    main()
