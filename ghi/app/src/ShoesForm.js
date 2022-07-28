import React from 'react';

class ShoesForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            manufacturer: '',
            model: '',
            color: '',
            picture: '',
            bins: [],
        };

        this.handleManufacturerChange = this.handleManufacturerChange.bind(this);
        this.handleModelCountChange = this.handleModelCountChange.bind(this);
        this.handleColorChange = this.handleColorChange.bind(this);
        this.handlePictureChange = this.handlePictureChange.bind(this);
        this.handleBinChange = this.handleBinChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    async componentDidMount() {
        const url = 'http://localhost:8100/api/bins/';
        const response = await fetch(url);
        if (response.ok) {
            const data = await response.json();
            this.setState({ bins: data.bins });

        }
    }

    async handleSubmit(event) {
        event.preventDefault();
        const data = { ...this.state };
        console.log(data)
        delete data.bins;
        const shoesUrl = 'http://localhost:8080/api/shoes/';
        const fetchConfig = {
            method: "post",
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json',
            },
        };
        const response = await fetch(shoesUrl, fetchConfig);
        if (response.ok) {
            const newShoe = await response.json();
            console.log(newShoe);

            const cleared = {
                manufacturer: '',
                model: '',
                color: '',
                picture: '',
                bin: '',
            };
            this.setState(cleared);
        }
    }

    handleManufacturerChange(event) {
        const value = event.target.value;
        this.setState({ manufacturer: value })
    }
    handleModelCountChange(event) {
        const value = event.target.value;
        this.setState({ model: value })
    }
    handleColorChange(event) {
        const value = event.target.value;
        this.setState({ color: value })
    }
    handlePictureChange(event) {
        const value = event.target.value;
        this.setState({ picture: value })
    }
    handleBinChange(event) {
        const value = event.target.value;
        this.setState({ bin: value })
    }

    render() {
        return (
            <div className="row">
                <div className="offset-3 col-6">
                    <div className="shadow p-4 mt-4">
                        <h1>Create a new shoes</h1>
                        <form onSubmit={this.handleSubmit} id="create-location-form">
                            <div className="form-floating mb-3">
                                <input value={this.state.manufacturer} onChange={this.handleManufacturerChange}
                                    placeholder="Manufacturer" required type="text" name="manufacturer"
                                    id="manufacturer" className="form-control" />
                                <label htmlFor="manufacturer">Manufacturer</label>
                            </div>
                            <div className="form-floating mb-3">
                                <input value={this.state.model} onChange={this.handleModelCountChange}
                                    placeholder="Model" required type="text" name="model"
                                    id="model" className="form-control" />
                                <label htmlFor="model">Model</label>
                            </div>
                            <div className="form-floating mb-3">
                                <input value={this.state.color} onChange={this.handleColorChange}
                                    placeholder="Color" required type="text" name="color"
                                    id="color" className="form-control" />
                                <label htmlFor="color">Color</label>
                            </div>
                            <div className="form-floating mb-3">
                                <input value={this.state.picture} onChange={this.handlePictureChange}
                                    placeholder="Picture" required type="text" name="picture"
                                    id="picture" className="form-control" />
                                <label htmlFor="picture">Picture</label>
                            </div>
                            <div className="mb-3">
                                <select value={this.state.bin} onChange={this.handleBinChange} required name="bin"
                                    id="bin" className="form-select">
                                    <option value="">Choose a bin</option>
                                    {this.state.bins.map(bin => {
                                        return (
                                            <option key={bin.id} value={bin.id}>{bin.closet_name}</option>
                                        );
                                    })}
                                </select>
                                <button className="btn btn-primary">Create</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        );
    }
}

export default ShoesForm;