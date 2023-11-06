import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import controlP5.*;
import processing.core.PApplet;

Textfield productosInput;
Connection dbConnection;
ControlP5 cp5;
Textarea dataTextArea;

String jdbcUrl = "jdbc:mysql://127.0.0.1:3306/mibasededatos";
String username = "root";
String password = "root";

void setup() {
  size(900, 900);
  background(255, 165, 0);
  cp5 = new ControlP5(this);

  productosInput = cp5.addTextfield("Control de produccion")
    .setPosition(150, 50)
    .setSize(400, 60)
    .setFont(createFont("Arial", 32))
    .setColorBackground(color(255, 165, 0))
    .setColorForeground(color(255))
    .setColorActive(color(0));

  cp5.addButton("Cargar Datos")
    .setPosition(350, 150)
    .setSize(200, 80)
    .setFont(createFont("Arial", 24))
    .setColorBackground(color(0))  
    .setColorForeground(color(0))
    .setColorActive(color ( 0));

  dataTextArea = cp5.addTextarea("Datos")
    .setPosition(50, 250)
    .setSize(800, 600)
    .setFont(createFont("Arial", 24))
    .setLineHeight(28)

    .setColorForeground(color(0));

  try {
    Class.forName("com.mysql.cj.jdbc.Driver");
    dbConnection = DriverManager.getConnection(jdbcUrl, username, password);
  } catch (ClassNotFoundException e) {
    println("Error al cargar el controlador JDBC: " + e.getMessage());
  } catch (SQLException e) {
    println("Error al conectar a la base de datos: " + e.getMessage());
  }
}

void draw() {
  // Tu código de dibujo si es necesario
}

void controlEvent(ControlEvent event) {
  if (event.isController()) {
    if (event.getController().getName().equals("Cargar Datos")) {
      String productos = productosInput.getText();
      cargarDatosDeTabla(productos);
    }
  }
}

void cargarDatosDeTabla(String Productos) {
  try {
    String consulta = "SELECT ID_Producto, Nombre, Stock FROM Productos";
    ResultSet resultSet = dbConnection.createStatement().executeQuery(consulta);
    String data = "";

    int graphCount = 0;
    while (resultSet.next()) {
      int id = resultSet.getInt("ID_Producto");
      String nombre = resultSet.getString("nombre");
      int stock = resultSet.getInt("Stock");

      data += "ID: " + id + ", control_de_produccion: " + nombre + ", pendiente: " + stock + "\n";

      // Calcular las coordenadas en el área del cuadro negro
      float x = 200 + (graphCount * 50); // Ajusta la posición X de cada gráfica
      float y = 900 - 50 - stock; // Ajusta la posición vertical desde abajo
      float barHeight = stock; // La altura de la barra coincide con el valor de "Stock"

      fill(255); // Color blanco
      rect(x, y, 20, barHeight); // Dibuja la barra en el área del cuadro 

      // Agregar el ID al centro de las gráficas en color negro
      textAlign(CENTER);
      fill(0); // Color negro
      text(id, x + 10, y - 10); 

      graphCount++;
    }

    println(data);
    dataTextArea.setText(data);
  } catch (SQLException e) {
    println("Error al cargar datos de la tabla: " + e.getMessage());
  }
}





void keyPressed() {
  if (key == 'q' || key == 'Q') {
    try {
      if (dbConnection != null) {
        dbConnection.close();
        println("Conexión cerrada.");
      }
    } catch (SQLException e) {
      println("Error al cerrar la conexión: " + e.getMessage());
    }
    exit();
  }
}
