#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define CityNo    9         //都市の数

#define rnd()     ( (double)rand() / RAND_MAX )     //乱数を発生

void initialize(void);
int update_state(void);
void display_state(int);
double energy(void);

double distance[CityNo][CityNo];    //都市間の距離
double unitout[CityNo][CityNo]; //初期値の設定

double Acoef = 1.0;
double Bcoef = 1.0;
double Dcoef = 2.0;     //重みづけ定数の設定

struct { double x, y; } cityxy[CityNo] =
{ { 3.0, 4.0 }, { 2.0, 7.0 }, { 4.0, 7.0 }, { 5.0, 5.0 },
    { 5.0, 3.0 }, { 4.0, 1.0 }, { 9.0, 1.0 }, { 1.0, 3.0 },
    { 1.0, 5.0 } };     //都市の位置設定

char endFlag = 0;       //終了フラグ
    
void main()
{
    int no = 1;     //試行回数
    double en;      //エネルギー

    srand((unsigned)time(NULL));        //乱数の初期化
    initialize();                       //初期化
    display_state( 0 );                 //試行0回目の表示
    update_state();                     //定数の更新

    for( no = 1; no < 50; no++ ){           //試行回数
        endFlag = update_state();           //重みづけ定数の更新
        display_state(no);                  //試行結果を表示
        en = energy();                      //エネルギーの計算
        printf(" Energy = %lf\n",en);       //エネルギーの表示
        if(endFlag == 1)    break;          //答えが出たら終了
    }
}

//初期化
void initialize()
{
    int i, j;
    double dtotal;      //合計距離

    dtotal = 0.0;
    for(i=0; i<CityNo; i++){
        for(j=0; j<CityNo; j++){
        distance[i][j] = 0.1 *
            sqrt((cityxy[i].x - cityxy[j].x) * (cityxy[i].x - cityxy[j].x) +
            (cityxy[i].y - cityxy[j].y) * (cityxy[i].y - cityxy[j].y)); //2都市間の距離を算出
            dtotal += distance[i][j];
        }                                           //合計距離の算出
    }
  
    for(i=0; i<CityNo; i++){
        for(j=0; j<CityNo; j++)
            distance[i][j] = 10.0 * distance[i][j] / dtotal;
    }

    for(i=0; i<CityNo; i++){
        for(j=0; j<CityNo; j++)
            unitout[i][j] = rnd();      //初期値に乱数を発生
    }
}

//定数の更新
int update_state()
{
    int    i, j, n, m, jm, jp;
    double un, unitin;              //入力
    double aterm, bterm, dterm;     //項
    int col[CityNo];                //列
    int row[CityNo];                //行
    int result = 1;                 //試行結果の検証
    
    for(i=0; i<CityNo; i++){        //行列の初期化
        col[i] = 0;
        row[i] = 0;
    }

    for(i=0; i<CityNo; i++){
        for(j=0; j<CityNo; j++){
            aterm = bterm = dterm = 0.0;
            for(n=0; n<CityNo; n++)
                aterm += unitout[i][n];
            aterm = -Acoef * (aterm - unitout[i][j]);                           //Ａ項の算出

            for(m=0; m<CityNo; m++)
                bterm += unitout[m][j];
            bterm = -Bcoef * (bterm - unitout[i][j]);                           //Ｂ項の算出

            if(j-1 == -1) jm = CityNo - 1;
            else jm = j - 1;
            if(j+1 == CityNo) jp = 0;
            else jp = j + 1;
            for(m=0; m<CityNo; m++)
                dterm += distance[i][m] * (unitout[m][jp] + unitout[m][jm]);
            dterm = -Dcoef * dterm;                                             //Ｄ項の算出

            unitin = aterm + bterm + dterm + Acoef + Bcoef;                     //入力値
            unitout[i][j] = 0.5 * (1.0 + tanh(unitin / 0.5));                   //出力値
        
            if(unitout[i][j] > 0.9){
                col[j] += 1;                    //列内で発火したニューロンの合計
                row[i] += 1;                    //行内で発火したニューロンの合計
            }
            
        }
    }
    
    for(i=0; i<CityNo; i++)
        result *= (col[i] * row[i]);            //結果を検証
    
    return (result == 1 ? 1 : 0);               //各行，各列で1つづつニューロンが発火していれば終了
}

//試行結果を表示
void display_state(int n)
{
  int    i, j;

    printf("    ###   Sequence     Cycle : %4d   ###\nCity ",n );
    for(i= 0; i<CityNo; i++)
        printf(" %4d  ",i+1);
    printf("\n");
    for(i=0; i<CityNo; i++){
        printf("%4d  ",i+1);
        for(j=0; j<CityNo; j++){
            printf("%5.2f  ",unitout[i][j]);
        }
        printf("\n");
    }
}

//エネルギーの計算
double energy()
{
  int    i, j, m, jp, jm;
  double term1, term2, term3;

  term1 = term2 = term3;

    for(i=0; i<CityNo; i++)
        for(j=0; j<CityNo; j++)
            for(m=0; m<CityNo; m++)
                if(m != j) term1 += unitout[i][j] * unitout[i][m];
    term1 = 0.5 * Acoef * term1;

    for(j=0; j<CityNo; j++)
        for(i=0; i<CityNo; i++)
            for(m=0; m<CityNo; m++)
                if(m != i) term2 += unitout[i][j] * unitout[m][j];
    term2 = 0.5 * Bcoef * term2;

    for(i=0; i<CityNo; i++){
        for(j=0; j<CityNo; j++){
            if(j-1 == -1) jm = CityNo - 1;
            else jm = j - 1;
            if(j+1 == CityNo) jp = 0;
            else jp = j + 1;
            for(m=0; m<CityNo; m++)
                term3 += distance[i][m] * unitout[i][j] * (unitout[m][jp] + unitout[m][jm]);
        }
    }
    term3 = 0.5 * Dcoef * term3;

    return (term1 + term2 + term3);
}


