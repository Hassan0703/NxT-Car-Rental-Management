# 🚗 Car Rental Management System

<div align="center">

![Car Rental](https://img.shields.io/badge/Car-Rental-blue)
![Frappe Framework](https://img.shields.io/badge/Frappe-Framework-green)
![Python](https://img.shields.io/badge/Python-3.10+-yellow)
![HTML/CSS/JS](https://img.shields.io/badge/HTML%2FCSS%2FJS-Website-orange)

**A comprehensive car rental management system built with Frappe Framework, featuring a modern web interface for seamless car rental operations.**

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Core Modules](#-core-modules)
- [Web Interface](#-web-interface)
- [API Endpoints](#-api-endpoints)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

The Car Rental Management System is a full-featured web application designed to streamline car rental operations. Built on the robust Frappe Framework, it provides a comprehensive solution for managing vehicles, customers, rental agreements, and billing processes. The system features a modern, responsive web interface that ensures excellent user experience across all devices.

### Key Benefits
- **Efficient Management**: Streamlined processes for car inventory, customer management, and rental operations
- **Modern UI/UX**: Beautiful, responsive design with intuitive navigation
- **Comprehensive Features**: Complete solution covering all aspects of car rental business
- **Scalable Architecture**: Built on Frappe Framework for enterprise-grade reliability

---

## ✨ Features

### 🚙 Vehicle Management
- **Car Inventory**: Complete vehicle database with brands, models, and specifications
- **Availability Tracking**: Real-time status monitoring for all vehicles
- **Pricing Management**: Flexible pricing packages and rate management
- **Image & Video Gallery**: Rich media support for vehicle showcase

### 👥 Customer Management
- **Customer Profiles**: Comprehensive customer information management
- **Driver Verification**: Driving license validation and verification
- **Contact Management**: Multiple communication channels support
- **Booking History**: Complete rental history and preferences

### 📋 Rental Operations
- **Rental Agreements**: Automated agreement generation and management
- **Booking System**: Seamless reservation and scheduling
- **Service Options**: With/without driver services
- **Billing & Payments**: Automated billing and payment tracking

### 🎨 Web Interface
- **Responsive Design**: Mobile-first approach for all devices
- **Modern UI**: Beautiful animations and smooth interactions
- **SEO Optimized**: Search engine friendly structure
- **Fast Loading**: Optimized performance and caching

---

## 🛠️ Technology Stack

### Backend
- **Framework**: [Frappe Framework](https://frappeframework.com/) v15.0+
- **Language**: Python 3.10+
- **Database**: MySQL/PostgreSQL (via Frappe)
- **Architecture**: MVC Pattern with DocType system

### Frontend
- **HTML5**: Semantic markup and modern structure
- **CSS3**: Advanced styling with animations and responsive design
- **JavaScript**: Interactive functionality and dynamic content
- **Bootstrap**: Responsive grid system and components
- **jQuery**: DOM manipulation and AJAX operations

### Libraries & Plugins
- **Font Awesome**: Icon library for enhanced UI
- **Owl Carousel**: Image and content sliders
- **Magnific Popup**: Lightbox and modal functionality
- **Select2**: Enhanced select dropdowns
- **Datepicker**: Date selection components

---

## 📁 Project Structure

```
app1/
├── app1/
│   ├── doctype/           # Data models and business logic
│   │   ├── car_brand/     # Car brand management
│   │   ├── car_details/   # Vehicle information
│   │   ├── car_team/      # Team member management
│   │   ├── car_type/      # Vehicle categorization
│   │   ├── customer_details/ # Customer profiles
│   │   ├── rental_agreement/ # Rental contracts
│   │   └── drivers/       # Driver management
│   ├── templates/         # HTML templates
│   ├── www/              # Web pages and frontend
│   └── config/           # Configuration files
├── public/               # Static assets
│   ├── css/             # Stylesheets and themes
│   ├── js/              # JavaScript files
│   ├── img/             # Images and media
│   └── fonts/           # Custom fonts
└── hooks.py             # Frappe hooks and events
```

---

## 🚀 Installation

### Prerequisites
- Python 3.10 or higher
- Frappe Framework v15.0+
- MySQL/PostgreSQL database
- Node.js and npm (for frontend assets)

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd app1
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Frappe Setup**
   ```bash
   bench get-app app1
   bench install-app app1
   ```

4. **Database Migration**
   ```bash
   bench migrate
   ```

5. **Start Development Server**
   ```bash
   bench start
   ```

---

## 💻 Usage

### Accessing the Application
- **URL**: `http://localhost:8000/app1`
- **Default Admin**: Administrator (configured during setup)

### Key Workflows

1. **Vehicle Management**
   - Add new car brands and models
   - Upload vehicle images and details
   - Set pricing and availability

2. **Customer Registration**
   - Create customer profiles
   - Verify driving licenses
   - Manage contact information

3. **Rental Process**
   - Create rental agreements
   - Select vehicles and services
   - Generate invoices and bills

4. **Web Interface**
   - Browse available vehicles
   - View pricing packages
   - Contact support team

---

## 🔧 Core Modules

### Car Management
- **Car Brand**: Brand categorization and management
- **Car Details**: Complete vehicle specifications
- **Car Type**: Vehicle classification system
- **Car Transmission**: Manual/Automatic options

### Customer Operations
- **Customer Details**: Profile management
- **Sign Up Details**: Registration process
- **Drivers**: Driver information and verification
- **Team**: Staff and team management

### Rental Operations
- **Rental Agreement**: Contract generation and management
- **Customer Bill**: Automated billing system
- **Data**: Analytics and reporting
- **Contact Us**: Customer support integration

---

## 🌐 Web Interface

### Main Pages
- **Home**: Landing page with featured vehicles
- **About**: Company information and story
- **Services**: Available rental services
- **Cars**: Vehicle catalog and details
- **Team**: Staff and team information
- **Contact**: Support and communication

### Features
- **Responsive Design**: Mobile-optimized layout
- **Image Gallery**: High-quality vehicle photos
- **Video Gallery**: Vehicle demonstration videos
- **Blog System**: Content management and updates
- **FAQ Section**: Common questions and answers
- **Testimonials**: Customer reviews and feedback

---

## 🔌 API Endpoints

The system provides RESTful API endpoints for:
- Vehicle management and queries
- Customer registration and authentication
- Rental agreement processing
- Billing and payment operations
- Reporting and analytics

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 Python coding standards
- Use meaningful commit messages
- Test thoroughly before submitting
- Update documentation as needed

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Support

- **Email**: support@nextash.com
- **Phone**: +92 308 3077 165
- **Website**: [NexTash](https://nextash.com)

---

## 🙏 Acknowledgments

- **Frappe Framework** team for the robust foundation
- **Bootstrap** for the responsive design framework
- **Font Awesome** for the beautiful icon library
- **All contributors** who helped shape this project

---

<div align="center">

**Built with ❤️ by NexTash Team**

*Making car rental management simple and efficient*

</div>