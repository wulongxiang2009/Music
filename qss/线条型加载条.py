LoadingBarA::LoadingBarA(QWidget *parent) :
    QWidget(parent)
{
    timer = new QTimer(this); //定时器
    timer->setInterval(50);
    connect(timer,QTimer::timeout,this,[=](){
        if(pointRect<=rectCount){
            pointRect++;
        }else{
            pointRect = pointRect%rectCount;
        }
        update();
    });
}

void LoadingBarA::paintEvent(QPaintEvent *event){ //重绘事件
    int width = this->width();
    int height = this->height();
    int side = qMin(width, height);

    QPainter painter(this);
    painter.setRenderHints(QPainter::Antialiasing | QPainter::TextAntialiasing);
    painter.translate(width / 2, height / 2);
    painter.scale(side / 200.0, side / 200.0);

    float degree = 360.0/rectCount; //rectCount:共有多少根线条

    for(int i =0;i<rectCount;i++){
        painter.rotate(degree);
        if(i == pointRect - 1){
            drawRect(&painter,darkColor); //突出颜色
        }else{
            drawRect(&painter,lightColor);//非突出颜色
        }
    }
}

void LoadingBarA::drawRect(QPainter* painter,QColor color){//画线条
    painter->save();
    painter->setPen(Qt::NoPen);
    painter->setBrush(color);
    QRect rect(arcLength,-rectHeight/2,rectWidth,rectHeight);
    painter->drawRoundedRect(rect,rectHeight/2,rectHeight/2);
    painter->restore();
}

void LoadingBarA::setDarkColor(QColor tempColor){
    this->darkColor = tempColor;
    update();
}

void LoadingBarA::setLightColor(QColor lightColor){
    this->lightColor = lightColor;
    update();
}

void LoadingBarA::setRectWidth(int l){
    this->rectWidth = l;
    update();
}

void LoadingBarA::setRectHeight(int l){
    this->rectHeight = l;
    update();
}

void LoadingBarA::setArcLength(int l){
    this->arcLength = l;
    update();
}

void LoadingBarA::setRectCount(int l){
    this->rectCount = l;
    update();
}

void LoadingBarA::startLoading(){ //设置开始
    timer->start();
}

