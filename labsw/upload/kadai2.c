/* 日付
 * 氏名・年齢を1行ずつファイルに出力するプログラム
 * 書き出すファイル名は実行時に引数で与える
 * 低水準関数を用いる
 */
#include <stdio.h>
#include <fcntl.h>

// 氏名・年齢
char name[20] = "Tezuka Shiori\n";
int age = 20;
// エラーメッセージ
char error[8] = "error!\n";

int main(int argc, char *argv[]){
  // エラー処理1
  if(argc != 2){
    write(2, error, 8);
    return -1;
  }
  // ファイルディスクリプタの宣言
  int fd;
  // writeエラー処理用変数
  int wr;

  /*  ファイルのオープン
   * 0_WRONLY : 書き込み専用
   * 0_CREAT : ファイルが存在しない場合新規作成
   * (このフラグを用いる場合ファイルのパーミッションを第3引数で指定する)
   * 0_TRUNK : ファイルサイズを0に切り詰める
   */
  fd = open(argv[1], O_WRONLY|O_CREAT|O_TRUNC, 0644);
  // エラー処理2
  if(fd == EOF){
    write(2, error, 8);
    return -1;
  }

  // int型をchar型の配列に変える
  char AGE[2];
  // ageを位ごとにわける
  int age10 = age / 10;
  int age1 = age % 10;
  // ASCIIコードにおける位置の割り出し
  AGE[0] = age10 + '0';
  AGE[1] = age1 + '0';

  wr = write(fd, name, 20);
  // エラー処理3
  if(wr == EOF){
    write(2, error, 8);
    return -1;
  }
  wr = write(fd, AGE, 2);
  // エラー処理4
  if(wr == EOF){
    write(2, error, 8);
    return -1;
  }

  // 処理の終了
  close(fd);
  return 0;
}

